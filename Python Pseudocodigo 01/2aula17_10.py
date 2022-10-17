"""
5)	Faça um programa que receba a altura e o sexo de uma pessoa e que calcule e mostre o seu peso ideal, utilizando as seguintes fórmulas:
a.	Para homens: (72.7 * h) – 58
b.	Para mulheres: (62.1 * h) – 44.7

"""

print("Digite a altura")
altura = float(input())
print("Digite o sexo (masculino/feminino)")
sexo = input()
if sexo == "Masculino" or sexo == "masculino":
    peso = (72.7 * altura) - 58
else: 
    peso = (62.1 * altura) - 44.7
print("O peso é: ", peso)