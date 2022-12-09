from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def home(request):
	pessoas = Pessoa.objects.all()
	return render(request,'index.html', {'pessoas': pessoas})

#View do form

def salvar(request):
	vnome = request.POST.get("nome")
	#Salvar
	Pessoa.objects.create(nome=vnome)
	pessoas = Pessoa.objects.all()
	return render(request,'index.html', {'pessoas': pessoas})


def editar(request, id):
	pessoas = Pessoa.objects.get(id=id)
	return render(request,'index.html', {'pessoas': pessoas})