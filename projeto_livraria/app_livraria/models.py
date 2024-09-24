from django.db import models

class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=250)
    idade = models.IntegerField()
