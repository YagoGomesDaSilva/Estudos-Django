from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def processa_formulario(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    return HttpResponse(f'{nome} {email}')


