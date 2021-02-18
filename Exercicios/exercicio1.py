#Desenvolva um programa que calcule o ano de nascimento da pessoa, a partir da sua idade, e o IMC a partir do peso e da altura. 
# Após realizar os calculos printar esses valores na tela.

nome = "Matheus"
idade = 26
altura = 1.71
peso = 85.50
ano_atual= 2021

IMC = peso / altura**2
ano_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos e  {altura}m de altura.')
print(f'{nome} pesa {peso}kg e seu imc é  {IMC:.2f}.')
print(f'{nome} nasceu em  {ano_nascimento}.')

