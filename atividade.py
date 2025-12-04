#CODIGO 1
print("Vamos calcular o gasto da voltagem")
v = float(input("Qual é a potência em watts? "))
tempo = float(input("Qual o tempo usado (em horas)? "))
total = v * tempo / 1000  # Conversão para kWh
print("O resultado é:", total)

if total < 110:
    print("Baixa tensão")
elif total > 220:
    print("Alta tensão")
else:
    print("Tensão dentro do padrão")

#CODIGO 2
print("Vamos calcular seu consumo diário da voltagem")
w = float(input("Qual é a sua voltagem em watts? "))
t = float(input("Me informe seu tempo de uso em horas: "))
total = w * t / 1000  # Conversão para kWh
print("O resultado da potência é de", total, "kWh")

if total < 1:
    print("Voltagem baixa")
elif 1 <= total < 5:
    print("Voltagem moderada")
else:
    print("Voltagem alta")

#CODIGO 3
print("Qual a temperatura atual do seu sistema?")
t = float(input("Informe a temperatura: "))

if t < 70:
    print("Temperatura normal")
elif 70 <= t < 90:
    print("Alerta!")
else:
    print("Perigo de superaquecimento!")

#CODIGO 4
numero = int(input("Digite um valor: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

#CODIGO 5
w = float(input("Digite o valor em watts: "))
total = w / 1000  # Conversão para kW
print("O valor em kW será", total)

#CODIGO 6
def calcular():
    print("Calculadora")
    number = float(input("Informe seu primeiro número: "))
    number2 = float(input("Informe seu segundo número: "))
    
    total = number + number2
    print("Soma:", total)
    
    total = number - number2
    print("Subtração:", total)
    
    if number2 != 0:
        total = number / number2
        print("Divisão:", total)
    else:
        print("Não é possível dividir por zero.")
    
    total = number * number2
    print("Multiplicação:", total)

calcular()

#CODIGO 7
print("Vamos identificar o valor em dBm")
v = float(input("Qual é o valor em dBm? "))

if v > -50:
    print("Excelente")
elif -70 < v <= -50:
    print("Bom")
else:
    print("Fraco")

#CODIGO 8
print("Bem-vindo à rede SENAI")
senha = input("Informe a senha: ")

if senha == "senai2025":
    print("Acesso permitido")
else:
    print("Acesso negado")

#CODIGO 9
on = input("Seu PC está ligado? (sim/não): ")

if on.lower() == "sim":
    print("Funcionando normalmente")
elif on.lower() == "não":
    print("Aguardando acionamento")
else:
    print("Resposta inválida!")

#CODIGO 10
print("Comparador de números")
number1 = int(input("Informe o primeiro número: "))
number2 = int(input("Informe o segundo número: "))

if number1 == number2:
    print("Os números são iguais")
else:
    maior = number1 if number1 > number2 else number2
    print("O maior número é", maior)

#CODIGO 11
print("Comparador de números")
number1 = int(input("Informe o primeiro número: "))
number2 = int(input("Informe o segundo número: "))

if number1 == number2:
    print("Os números são iguais")
else:
    maior = number1 if number1 > number2 else number2
    print("O maior número é", maior)

#CODIGO 12
material = input("Escolha um material para saber se ele é condutor: ").lower()

if material == "alumínio" or material == "cobre":
    print("Condutor")
else:
    print("Não condutor")

#CODIGO 13
A = float(input("Qual é o valor da corrente elétrica (em amperes)? "))

if A > 30:
    print("Sobrecarga detectada")
else:
    print("Corrente dentro do limite")

#CODIGO 14
print("Processando o sistema")
falha = input("O sistema apresenta falhas? (sim/não): ").lower()

if falha == "sim":
    print("O botão de emergência foi acionado.")
else:
    print("A operação segue normalmente.")

#CODIGO 15
num1 = int(input("Informe o valor primário: "))

if num1 == 0:
    print("Sinal baixo")
elif num1 == 1:
    print("Sinal alto")
else:
    print("Valor inválido")

#CODIGO 16
sensor = int(input("Quanto tempo de uso tem o seu sensor (em anos)? "))

if sensor >= 5:
    print("Substituição recomendada")
else:
    print("Sensor dentro do prazo")

#CODIGO 17
n1 = int(input("Diga-me o número do seu sistema (1 para monofásico, 2 para bifásico, 3 para trifásico): "))

if n1 == 1:
    print("Sistema monofásico")
elif n1 == 2:
    print("Sistema bifásico")
elif n1 == 3:
    print("Sistema trifásico")
else:
    print("Opção inválida")

#CODIGO 18
ppm = int(input("Digite a concentração de partículas: "))

if ppm < 100:
    print("Ambiente seguro")
elif 100 <= ppm <= 200:
    print("Atenção")
else:
    print("ALARME: Risco de incêndio")

#CODIGO 19
h = int(input("Qual horário você trabalha? (em 24h): "))

if 6 <= h <= 13:
    print("Turno da manhã")
elif 14 <= h <= 21:
    print("Turno da tarde")
else:
    print("Turno da noite")

#CODIGO 20
system = input("Seu circuito está fechado? (s/n): ").lower()

if system == "s":
    print("Circuito com continuidade")
elif system == "n":
    print("Circuito aberto")
else:
    print("Resposta inválida!")