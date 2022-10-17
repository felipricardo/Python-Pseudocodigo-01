"""
3)	Efetuar o cálculo e a apresentação do valor de uma prestação em atraso, 
utilizando a fórmula: PRESTACAO = VALOR + (VALOR *(TAXA/100) * TEMPOEMDIAS).
"""

print ("Digite o valor da prestação")
valor = float(input ())
print("Digite o perc da taxa")
taxa = float(input())
print("Digite o tempo em dias de atraso")
tempoemdias = int(input())
prestacao = valor + ((valor * (taxa / 100)) * tempoemdias
print("O valor da pestação e", prestacao)