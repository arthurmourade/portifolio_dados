# exercicio
nome = "joao paulo lira"
email = "emailfalsolira@gmail.com"

# descubra o servidor do email
posicao = email.find("@")
print(posicao)
servidor = email[posicao:]
# descubra o 1° nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
primeiro_nome = nome.capitalize()
print(primeiro_nome)

# criar uma mensagem personalizada

mensagem = f"O usuário {primeiro_nome} foi cadastrado com sucesso no email {email}"
print(mensagem)