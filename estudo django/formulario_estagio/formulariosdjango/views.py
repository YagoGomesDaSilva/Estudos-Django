from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

def home(request):
    form = formularioCadastro()
    return render(request,'home.html',{'form':form})

def processa_formulario(request):
    form = formularioCadastro(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("salvo com sucesso")
    else:
        return HttpResponse("erro no sistema")
