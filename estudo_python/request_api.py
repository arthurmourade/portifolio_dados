import requests # Importa a biblioteca HTTPS

import json # Importa a biblioteca Json, que permite lermos requisições de API

def extrair_dados(endpoint): # Define a função e o parâmetro
    response = requests.get(endpoint) # Define a variável "response" para obter dados da API
    if response.status_code == 200: # Define uma condição para testar a conexão
        return.json() # Se a conexão estiver correta, ele extrai os dados da API em formato Json
    else:
        print:(f"Erro ao extrair os dados do {endpoint}") # Se a condição não for verdadeira, ele traz o erro da requisição
        return None # Retorna 'None' para quebrar o fluxo e parar a automação

endpoint_user = "https://dummyjson.com/users/" # Variável que armazena os dados da API relacionada aos usuários
endpoint_product = "https://dummyjson.com/products/" # Variável que armazena os dados da API relacionada aos produtos

data_users = extrair_dados(endpoint_user) # Variável que armazena o resultado da função
data_product = extrair_dados(endpoint_product) # Variável que armazena o resultado da função

print(data_users) # Imprime o resultado