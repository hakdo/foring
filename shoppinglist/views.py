from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import SimpleList
from . forms import SimpleListForm, loginForm, registernewForm
# Create your views here.

def init(request):
    return render(request,'shoppinglist/init.html',{})

@login_required(login_url='/login/')
def createlist(request):
    if request.method=='POST':
        form = SimpleListForm(request.POST)
        if form.is_valid():
            new_shoppinglist = form.save(commit=False)
            new_shoppinglist.owner = request.user.username
            new_shoppinglist = form.save()
            return redirect('myshoppinglists')
        else:
            return HttpResponse('Error')
    else:
        form = SimpleListForm()
        return render(request, 'shoppinglist/createlist.html', {'form': form})

@login_required(login_url='/login/')
def myshoppinglists(request):
    # Users not included yet, getting all lists
    shopping_lists = SimpleList.objects.filter(finished=False, owner=request.user.username)
    return render(request, 'shoppinglist/my_shopping_lists.html', {'lists': shopping_lists})

def list_detail(request, pk):
    current_list = get_object_or_404(SimpleList, pk=pk)
    if request.method =='POST':
        current_list.finished = True
        current_list.save()
        return redirect('myshoppinglists')
    else:
        list_items=current_list.contents.split()
        return render(request, 'shoppinglist/list_detail.html', {'list': current_list, 'items': list_items})

def userlogin(request):
    if request.method == 'POST':
        userdata = loginForm(request.POST)
        if userdata.is_valid():
            user = authenticate(username=userdata.cleaned_data['username'],password=userdata.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('init')
                else:
                    return HttpResponse('Konto er ikke aktiv.')
            else:
                return HttpResponse('Ugyldig forsøk på innlogging.')
        else:
            return HttpResponse('Ugyldig skjema')
    else:
        form = loginForm()
        return render(request,'shoppinglist/login.html',{'form': form})

def userlogout(request):
    logout(request)
    return redirect('init')

def newuser(request):
    if request.method == 'POST':
        new_user = registernewForm(request.POST)
        if new_user.is_valid():
            username = new_user.cleaned_data['username']
            email = new_user.cleaned_data['email']
            password=new_user.cleaned_data['password']
            try:
                user = User.objects.create_user(username,email,password)
                user.save()
                return redirect('welcome')
            except:
                return HttpResponse('Noe gikk feil. Prøv igjen med et annet brukernavn/passord.')
        else:
            return HttpResponse('Noe gikk feil. Dette skal ikke gå an. Hvordan fikk du til dette?')
    else:
        form = registernewForm()
        return render(request,'shoppinglist/register_new.html',{'form': form})

def welcome(request):
    return render(request,'shoppinglist/welcome.html',{})
