from django.shortcuts import render
from django.http import HttpResponse
from .forms import formularioCadastro

def home(request):
    form = formularioCadastro()
    return render(request,'home.html',{'form':form})

def processa_formulario(request):
    form = formularioCadastro(request.POST)
    if form.is_valid():
        nome = form.data['nome']
        email = form.data['email']
        return HttpResponse(f"{nome} {email}")
    else:
        return HttpResponse("erro no sistema")



