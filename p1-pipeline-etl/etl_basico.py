import csv
from posixpath import sep

with open(
    'clientes_sujo.csv', mode = 'r', sep =';', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
