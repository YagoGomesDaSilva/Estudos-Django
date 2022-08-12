from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    cell = models.CharField(max_length=11)
    email = models.EmailField()

    
    def __str__(self) -> str:
        return self.nome