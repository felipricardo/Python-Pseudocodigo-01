'''
2)	Construir um programa que efetue o cálculo do salário líquido de um professor. 
Para fazer este programa, você deverá possuir alguns dados, tais como: valor da hora aula, número de horas 
trabalhadas no mês e percentual de desconto do INSS. Em primeiro lugar, 
deve-se estabelecer qual será o seu salário bruto para efetuar o desconto e ter o valor do salário líquido.
ENTRADAS
- valhora
- numhoras
- percinss
PROCESSAMENTOS
salbruto = valhora * numhoras
valinss = (salbruto * percinss) / 100
salliq = salbruto - valinss
SAIDA
salbruto
valinss
salliq
'''
#entradas
print("Digite o valor o valor da hora")
valhora = float(input())
print("Digite o numero de horas")
numhoras = float(input())
print("Digite o percentual de INSS")
percinss = float(input())
#processamento
valbruto = valhora * numhoras
valinss = (valbruto * percinss) / 100
salliq = valbruto - valinss
#saidas
print("O valor do salario bruto e %.2f "% valbruto)
print("%.2f O valor do INSS e " % valinss)
print("O valor do salario liq e %.2f" % salliq)