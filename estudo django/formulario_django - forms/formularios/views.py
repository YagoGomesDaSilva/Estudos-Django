from django.shortcuts import render
from django.http import HttpResponse
from .forms import formularioCadastro

def home(request):
    form = formularioCadastro()
    return render(request,'home.html',{'form':form})

def processa_formulario(request):
    
    return HttpResponse('teste')


