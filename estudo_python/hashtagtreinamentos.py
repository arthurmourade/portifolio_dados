


from operator import pos


email = " ArthUrmouradea@gmail.com "

email = email.lower() # colocar em letra minúscula
email = email.strip() # ajustar espaços vazios
print(email)

# posição
posicao = email.find("@")
print(posicao)

# pedaços do texto
servidor = email[posicao:]
print(servidor)

# email_falso@gmail.com

# trocar um pedaço do texto
novo_email = email.replace("gmail.com", "yahoo.com.br")
print(novo_email)

nome = "arhtur Moura"
nome = nome.capitalize()
print(nome)
nome = nome.title()
print(nome)

# formatação numérica
faturamento = 2_000
custo = 1000
lucro = faturamento - custo
margem = lucro / faturamento

texto = f"O lucro foi de R${lucro:,.2f}, o faturamento foi de R${faturamento:,.2f} e a margem foi de {margem:.1%}"
print(texto)
