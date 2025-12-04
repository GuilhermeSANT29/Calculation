# Exercício 1: Imprima os números de 1 a 10 utilizando um for. for i in range(1, 11): 
 print(i) 

# Exercício 2: Imprima os números pares de 0 a 20. 
for i in range(0, 21, 2): 
 print(i) 

# Exercício 3: Imprima os números ímpares de 1 a 19. 
for i in range(1, 20, 2): 
 print(i) 

# Exercício 4: Imprima a tabuada do 5 (de 5x1 até 5x10). for i in range(1, 11): 
 print(f"5 x {i} = {5 * i}") 

# Exercício 5: Some todos os números de 1 a 10 e mostre o resultado. soma = 0 
for i in range(1, 11): 
 soma += i 
print(f"Soma de 1 a 10: {soma}") 

# Exercício 6: Peça ao usuário 5 números e calcule a média. soma = 0 
for i in range(5): 
 numero = float(input("Digite um número: ")) 
 soma += numero 
media = soma / 5 
print(f"A média dos números é: {media}") 

# Exercício 7: Imprima 10 vezes a frase "Estou aprendendo Python!". for i in range(10): 
 print("Estou aprendendo Python!")
 
# Exercício 8: Peça uma palavra ao usuário e imprima cada letra em uma linha. 
palavra = input("Digite uma palavra: ") 
for letra in palavra: 
 print(letra) 

# Exercício 9: Imprima uma escada com asteriscos. 
for i in range(1, 6): 
 print('*' * i)

# Exercício 10: Peça ao usuário para digitar uma frase e verifique se tem a letra 'a'. 
frase = input("Digite uma frase: ") 
if 'a' in frase: 
 print("A frase contém a letra 'a'.") 
else: 
 print("A frase não contém a letra 'a'.")

# Exercício 11: Peça um número n ao usuário e imprima a tabuada desse número. 
n = int(input("Digite um número para ver a tabuada: ")) for i in range(1, 11): 
 print(f"{n} x {i} = {n * i}") 

# Exercício 12: Peça dois números e imprima todos os números entre eles. 
inicio = int(input("Digite o primeiro número: ")) 
fim = int(input("Digite o segundo número: ")) 
for i in range(inicio + 1, fim): 
 print(i) 

# Exercício 13: Imprima os quadrados dos números de 1 a 10. for i in range(1, 11): 
 print(f"O quadrado de {i} é {i ** 2}") 

# Exercício 14: Imprima o cubo dos números de 1 a 20. for i in range(1, 21): 
 print(f"O cubo de {i} é {i ** 3}") 

# Exercício 15: Conte quantos múltiplos de 3 existem entre 1 e 100. contagem = 0 
for i in range(1, 101): 
 if i % 3 == 0: 
 contagem += 1 
print(f"Existem {contagem} múltiplos de 3 entre 1 e 100.") 

# Exercício 16: Peça 5 números ao usuário e imprima o dobro de cada número. 
for i in range(5): 
 numero = float(input("Digite um número: ")) 
 print(f"O dobro de {numero} é {numero * 2}")

 #PARTE 2

 # TABUADA DO 3 
for x in range (1, 11): 
 print (3*x) 
y = input ("digite uma palavra") 
for x in y :  
 if (x == "A" or x == "a"): 
 print ("vogal") 
 elif (x == "E" or x == "e"): 
 print ("vogal") 
 elif (x == "I" or x == "i"):  print ("vogal") 
 elif (x == "O" or x == "o"):  print ("vogal") 
 elif (x == "U" or x == "u"):  print ("vogal") 
 elif (x == " ") : 
 print ("digitou espaço") 
 else: 
 print ("consoante") 

#CODIGO 1 
# REPETIÇAO 
for x in range (1, 6): # 1 2 3 4 5  print ("ola, mundo", x)
 
#CODIGO 2 
for x in range (1, 11): 
 print (x) 

#CODIGO 3 
for x in range (1, 6) : 
 print ("esse e o numero de repetiçao", x) 

#CODIGO 4 
#tabuada do 9 
for x in range (1, 11) : 
 print (9*x) 

#CODIGO 5 
for x in range (1, 6) : 
 print (1+x)

#CODIGO 6 
name = input ("qual seu nome?") 
for x in range (1, 6): 
 print (name) 

#CODIGO 7 
for x in range (1, 6): 
 print ("ta estudando pyton", x) 

#CODIGO 8 
#numeros pares 
for x in range (0, 11): 
 if x % 2 == 0 : 
 print (x, "sao pares") 

#CODIGO 9 
frase = input ("digite sua frase iremos replicar") for x in range (0, 4): 
 print (frase)  

#CODIGO 10 
#contar vogais 
contador = 0 
word = "abracadabra" 
vogais = ["a", 'e', 'i', 'o', 'u'] 
for x in word: 
 if x in vogais: 
 contador += 1 
 else: 
 pass 
print ("total de vogais:", contador) 

#CODIGO 11 
for x in range (1, 5): 
 print ("contando", x) 

#CONTADOR 12 
#dobro triplo e quadriblo 
n = int (input("digite seu numero")) 
for x in range (1): 
 print ("dobro", n*2, "triplo", n*3, "quadriplo", n*4 )

