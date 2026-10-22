def calcular_imposto(valor): # Defino a função 
    if valor >= 1000:
        imposto = valor * 0.1
    elif valor > 2000:
        imposto = valor * 0.15
    else:
        imposto = valor * 0.25

    return imposto

preco_produto = 1000

produto_calculado = calcular_imposto(preco_produto)
print(produto_calculado)
