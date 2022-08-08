from django.db import models

#primiro passao para contruir a tabela e fazer as migrations
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.nome

