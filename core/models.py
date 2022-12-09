from django.db import models

# Create your models here.
class Pessoa(models.Model):
	#Criar um model
	nome = models.CharField(max_length=100)


	#Como imprimir
	def __str__(self):
		return self.nome