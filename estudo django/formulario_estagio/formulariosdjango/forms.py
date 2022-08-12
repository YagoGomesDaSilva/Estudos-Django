from django import forms
from .models import Pessoa

class formularioCadastro(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome','cpf','cell','email')