from django.shortcuts import render, get_object_or_404
from .models import Republica, Contato, Imagem
from.forms import RepublicaForms


# Create your views here.
def home(request):
    republicas = Republica.objects.all
    return render(request, 'home.html', {'republicas': republicas})

def pesquisar(request):
    pesquisa = request.POST.get('pesquisa')
    if Republica.objects.filter(bairro__icontains=pesquisa,):
        republicas = Republica.objects.filter(modelo__icontains=pesquisa,)
    elif Republica.objects.filter(cidade__icontains=pesquisa,):
        republicas = Republica.objects.filter(cor__icontains=pesquisa,)
    elif Republica.objects.filter(rua__icontains=pesquisa,):
        republicas = Republica.objects.filter(nome_republica__icontains=pesquisa,)
    else:
        republicas = Republica.objects.all()
    return render(request, 'home.html', {'republicas': republicas})


def sobre(request):
    return render(request,'sobre.html')


def contato(request):
    if request.method == "GET":
        return render(request, 'contato.html')
    elif request.method == "POST":
        contact = Contato()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.telefone = request.POST.get('telefone')
        contact.mensagem = request.POST.get('mensagem')

        contact.save()
        mensagem = "Mensagem enviada com sucesso"
        return render(request,'contato.html',{'mensagem': mensagem})


def anuncie(request):
    if request.method == "GET":
        form = RepublicaForms()
        return render(request, "anuncie.html", {'form': form})
    else:
        form = RepublicaForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
        return render(request, 'home.html')


def republica(request, id):
    republica = get_object_or_404(Republica, id=id)
    sugestoes = Republica.objects.filter(bairro=republica.cidade).exclude(id=id)[:2]
    return render(request, 'republica.html', {'republica': republica, 'sugestoes': sugestoes, 'id': id})

