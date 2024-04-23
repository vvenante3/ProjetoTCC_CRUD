from django.shortcuts import render, redirect
from .models import Policial
def home(request):
    policiais = Policial.objects.all()
    return render(request, "index.html", {"policiais": policiais})

def salvar(request):
    DataCadastro    = request.POST.get("DataCadastro")
    DataNascimento  = request.POST.get("DataNascimento")
    Sexo            = request.POST.get("Sexo")

    #Salvar no Db
    Policial.objects.create(DataCadastro=DataCadastro, DataNascimento=DataNascimento, Sexo=Sexo)
    policiais = Policial.objects.all()
    return render(request, "index.html", {"policiais": policiais})

def editar(request, id):
    policial = Policial.objects.get(idPolicial=id)
    return render(request, "atualizar.html", {"policial": policial})


def atualizar(request, id):
    DataCadastro   =    request.POST.get("DataCadastro")
    DataNascimento =    request.POST.get("DataNascimento")
    Sexo           =    request.POST.get("Sexo")

    policial = Policial.objects.get(idPolicial=id)

    policial.DataCadastro   = DataCadastro
    policial.DataNascimento = DataNascimento
    policial.Sexo           = Sexo
    policial.save()
    return redirect(home)

def deletar(request, id):
    policial = Policial.objects.get(idPolicial=id)
    policial.delete()
    return redirect("home")