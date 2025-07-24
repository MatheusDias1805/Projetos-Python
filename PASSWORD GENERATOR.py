import random

# PASSWORD GENERATOR!!

#Caracteres que vão ser usados para gerar a senha:
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxwyz,.;/][@#!$%&*()-=+_?:><]}{0123456789"

#Input de quantas senhas:
qtdade = int(input("Quantas senhas você precisa? "))

#Input do tamanho de cada senha:
tamanho = int(input("Qual o tamanho das senhas? "))

print("\nAqui estão suas senhas:")

#Para o valor da quantidade, o programa vai gerar uma senha aleatória usando o random com os caracteres no tamanho solicitado.
for cada in range(qtdade):
    passwords = ""
    for c in range(tamanho):
        passwords += random.choice(chars)

print(passwords)