import requests
import json
import matplotlib.pyplot as plt

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()

print(f'Valor atual do Dólar: {float(cotacoes_dic["USD"]["bid"]):.2f}')

cotacoes_dolar = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes_dolar_dic = cotacoes_dolar.json()

lista_cotacoes_dolar = [float(item['bid']) for item in cotacoes_dolar_dic]
lista_cotacoes_dolar.reverse()
print([f'{valor:.2f}' for valor in lista_cotacoes_dolar])

maior_valor_dolar = max(lista_cotacoes_dolar)
print(f'Maior valor nos últimos 30 dias: {maior_valor_dolar:.2f}')

plt.figure(figsize=(15, 8))
plt.plot(lista_cotacoes_dolar, marker='o')
plt.title('Valor do Dólar Nos Últimos 30 Dias')
plt.grid()

plt.show()