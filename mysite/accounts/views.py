from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.




def login_(request):
    if request.method =='POST':
        username= request.POST['email']
        password = request.POST['password']
        user_ = authenticate(username = username, password = password)
        if user_ is not None:
            if User.objects.filter(username=username).exists():
                login(request, user_)
                return redirect('index')
        else:
            messages.info(request,'Erro ao tentar logar')
            return redirect(request,'index')



def register(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():
            messages.info(request,'Usuário já cadastrado')
            return redirect('index')
        else:
            user = User.objects.create_user(username = username, password = password)
            return redirect('index')

def logout_(request):
    logout(request)
    return redirect('index')