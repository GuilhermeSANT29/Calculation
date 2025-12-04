#c tensao
print ("vamos calcular a tensão") 
r = float ( input ("digite a resistencia")) 
i = float ( input ("digite a corrente")) 
total = r * i 
print ("a tensao é", total,"v") 

#c Corrente
r = float(input("digite a resistencia")) 
v = float(input("digite a tensão ")) 
i = r / v 
print("a corrente é", i ) 

#c resistencia
print ("vamos calcular a resistencia") 
v = float ( input ("digite a tensao em volts")) 
i = float ( input ("digite a corrente em ampares")) total = v / i 
print ("a resistencia é", total,"ohms") 

#c Potencia
i = float(input("digite a resistencia")) 
v = float(input("digite a tensão ")) 
p = i * v 
print("a potencia é", p ) 

#c wats
print ("vamos calcular tempo e wats") 
p = float ( input ("digite a potencia em watts")) 
t = float ( input ("digite o tempo")) 
total = p * t 
print ("o resultado é", total,) 

#c Wh Kwh
Wh = float(input("digite o Wh que iramos converter em kWh")) kWh = Wh / 1000 
print("o resultado do kWh é", kWh ) 

#Crie um programa que calcule o com base na fórmula
print ("vamos calcular") 
kwh = float ( input ("digite o consumo de kwh")) v = float ( input ("digite o valor da tarifa")) 
total = kwh * v 
print ("o resultado é", total,) 

#calcule o que um equipamento pode funcionar com uma quantidade de energia disponível, usando a fórmula
E = float(input("digite o E que iramos converter em T")) P = float(input("digite o P")) 
t = E / P 
print("o resultado do T é", t )

#Python que converta um valor de tempo em horas para minutos e segundos.
print ("vamos calcular seu tempo, em minutos") h = float ( input ("digite o tempo em horas")) 
total = h * 60 
m = float ( input ("digite os minutos")) 
total2 = m * 60 
print ("o resultado é", total,"minutos e",total2,"em segundos") 

#calcule a em um fio condutor com base na fórmula
i = float(input("digite a corrente")) 
r = float(input("digite a resistencia")) 
vq = r * i 
print("o resultado deles sera de", vq )
