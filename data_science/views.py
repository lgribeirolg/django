from django.shortcuts import render


def index(request):
        return render(request,'data_science/index.html')

def imagem(request):
        return render(request, 'data_science/imagem.html')