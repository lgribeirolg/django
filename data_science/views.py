from django.shortcuts import render
import requests


def index(request):
        dados = cotacao()
        return render(request,'data_science/index.html',{'dados':dados})

def imagem(request):
        
        return render(request, 'data_science/imagem.html')

def cotacao():
        

        # URL do endpoint da CoinGecko para obter preços simples das criptomoedas
        url = 'https://api.coingecko.com/api/v3/simple/price'

        # Definindo as moedas que você quer buscar
        params = {
        'ids': 'bitcoin,ethereum,ripple',  # Moedas que você quer obter preço
        'vs_currencies': 'eur',  # Moeda para comparação (exemplo: USD)
        }

        # Fazendo a requisição para a API
        response = requests.get(url, params=params)

        # Verificando se a requisição foi bem sucedida (status code 200)
        if response.status_code == 200:
                data = response.json()
                # Exibindo os preços das criptomoedas em USD
                #print(f"Bitcoin Price: ${data['bitcoin']['usd']}")
                #print(f"Ethereum Price: ${data['ethereum']['usd']}")
                #print(f"Ripple Price: ${data['ripple']['usd']}")
        else:
                erro = (f"Error: {response.status_code}")

        return data