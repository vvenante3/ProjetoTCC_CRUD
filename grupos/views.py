from django.shortcuts import render, redirect
from .models import Policial, Psicologo

# POLICIAL (PARTICIPANTES)
def home(request):
    policiais = Policial.objects.all()
    return render(request, "index.html", {"policiais": policiais})

def salvar(request):
    Matricula       = request.POST['Matricula']
    Nome            = request.POST['Nome']
    Sobrenome       = request.POST['Sobrenome']
    DataCadastro    = request.POST.get("DataCadastro")
    DataNascimento  = request.POST.get("DataNascimento")
    Sexo            = request.POST.get("Sexo")

    #Salvar no Db
    Policial.objects.create(Matricula=Matricula, Nome=Nome, Sobrenome=Sobrenome, DataCadastro=DataCadastro, DataNascimento=DataNascimento, Sexo=Sexo)
    policiais = Policial.objects.all()
    return redirect(home)

def editar(request, id):
    policial = Policial.objects.get(idPolicial=id)
    return render(request, "atualizar.html", {"policial": policial})

def atualizar(request, id):
    Matricula      = request.POST.get('Matricula')
    Nome           = request.POST.get('Nome')
    Sobrenome      = request.POST.get('Sobrenome')
    DataCadastro   =    request.POST.get("DataCadastro")
    DataNascimento =    request.POST.get("DataNascimento")
    Sexo           =    request.POST.get("Sexo")

    policial = Policial.objects.get(idPolicial=id)

    policial.Matricula      = Matricula
    policial.Nome           = Nome
    policial.Sobrenome      = Sobrenome
    policial.DataCadastro   = DataCadastro
    policial.DataNascimento = DataNascimento
    policial.Sexo           = Sexo
    policial.save()
    return redirect(home)

def deletar(request, id):
    policial = Policial.objects.get(idPolicial=id)
    policial.delete()
    return redirect(home)

# PSICOLOGO
def home_psicologo(request):
    psicologo = Psicologo.objects.all()
    return render(request, "index_psicologo.html", {"psicologo": psicologo})

def salvar_psicologo(request):
    NomePsicologo       = request.POST.get('NomePsicologo')
    CRP                 = request.POST.get('CRP')

    # Salvar no Db
    Psicologo.objects.create(NomePsicologo=NomePsicologo, CRP=CRP)
    psicologos = Psicologo.objects.all()
    return redirect('home_psicologo')

def editar_psicologo(request, id):
    psicologo = Psicologo.objects.get(idPsicologo=id)
    return render(request,"atualizar_psicologo.html", {"psicologo": psicologo})

def atualizar_psicologo(request, id):
    NomePsicologo = request.POST.get('NomePsicologo')
    CRP = request.POST.get('CRP')

    psicologo = Psicologo.objects.get(idPsicologo=id)

    psicologo.NomePsicologo = NomePsicologo
    psicologo.CRP           = CRP
    psicologo.save()
    return redirect('home_psicologo')

def deletar_psicologo(request, id):
    psicologo = Psicologo.objects.get(idPsicologo=id)
    psicologo.delete()
    return redirect('home_psicologo')

# BARRA DE BUSCA
def search_view(request):
    query = request.GET.get('matricula')

    if query:
        policiais = Policial.objects.filter(Matricula__icontains=query)
    else:
        policiais = Policial.objects.all()

    return render(request, 'search.html', {'policiais': policiais, 'query':query})

