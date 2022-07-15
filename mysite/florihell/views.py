from django.shortcuts import redirect, render
from .models import Produto

# Create your views here.

def index(request):

    produto_all = Produto.objects.all()

    context={
        'produto_all':produto_all
    }

    return render(request,'index.html',context)

def register_pag(request):
    return render(request,'register.html')


def signin_pag(request):
    return render(request,'signin.html')

def cart_pag(request):
    return render(request,'cart.html')

def checkout_pag(request):
    return render(request,'checkout.html')
