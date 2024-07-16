import xmltodict

def nomes_moedas():
with open("moedas.xml","rb") as arquivo_moedas:
     dic_moedas = xmltodict.parce(arquivo_moedas)

moedas = dic_moedas["xml"]
return moedas
print(moedas)

with open("conversoes.xml","rb") as arquivo_conversores:
     dic_conversoes = xmltodict.parce(arquivo_conversores)

conversoes = dic_conversoes["xml"]
print(conversoes)