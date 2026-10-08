# Exercícios Python

# Exercício 1

def somar(a, b):
    resultado = a + b
    return resultado

print(somar(5, 6))

# Exercício 2

def saudacao(nome):
    mensagem = ('Olá, ' + nome + '!')
    return mensagem

print(saudacao('Ana'))

# Exercício 3

def aplicar_desconto(preco, desconto):
    pergunta = preco -(preco * desconto / 100)
    return pergunta

print(aplicar_desconto(180, 30))


# Exercicio 4

def verificar_idade(idade):
    if idade >= 18:
        return ('maior de idade')
    else:
        return 'menor de idade'

print(verificar_idade(19))

# Exercicio 5

def situacao_aluno(nota):
    if nota >= 7:
        return ('aprovado')
    elif nota >= 5 and nota < 7:
        return ('recuperacao')
    else:
        return ('reprovado')

print(situacao_aluno(7))
print(situacao_aluno(6))
print(situacao_aluno(4))

# Exercício 6

def validar_valor(valor):
    if valor is None:
        return "invalido"
    elif valor < 0:
        return "invalido"
    else:
        return "valido"

print(validar_valor(100))    # valido
print(validar_valor(0))      # valido (limite)
print(validar_valor(-5))     # invalido
print(validar_valor(None))   # invalido


vendas = [100, 250, 80, 400]
nomes = ["Ana", "Caio", "Bia"]

for venda in vendas:
    print(vendas * 2)

