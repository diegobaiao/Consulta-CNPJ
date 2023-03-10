import requests
import json


cnpj = input(str("Digite um cnpj: "))


def editar_cnpj(cnpj):
    cnpj = str(cnpj).replace('.','').replace('/','').replace('-','')
    
    while len(cnpj) != 14:
        cnpj = '0' + cnpj
    return cnpj


cnpj = editar_cnpj(cnpj)


def api_cnpj(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"}
    response = requests.request("GET", url, params=querystring)
    resp = json.loads(response.text)
    x = resp['cnpj']
    y = resp['nome']
    z = resp['situacao']
    print(f"O CNPJ {x} pertence a empresa {y} e sua situação cadastral se encontra {z}")


api_cnpj(cnpj)
