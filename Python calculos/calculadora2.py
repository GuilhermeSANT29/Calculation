# Função para realizar cálculos simples de adição, subtração, multiplicação e divisão
def calculate():
    # Solicita ao usuário a operação matemática desejada
    operation = input(''' 
    Please type in the math operation you would like to complete: 
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    
    # Solicita ao usuário os dois números
    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))
    
    # Verifica a operação e executa o cálculo
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        if number_2 != 0:
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)
        else:
            print("Error: Division by zero!")
    else:
        print('You have not typed a valid operator, please run the program again.')

# Função para cálculos de resistência, corrente, potência e tensão
def calculate2():
    # Solicita ao usuário a operação a ser realizada
    operation2 = input(''' 
    Sistemas avançados! 
    Calcular resistências R = V / I
    Cálculo de corrente I = V / R
    Calcular potência P = V * I
    Cálculo de tensão V = R * I
    ''')

    # Solicita os valores dos números
    number_1 = float(input('Please enter the first number (e.g., voltage or current): '))
    number_2 = float(input('Please enter the second number (e.g., resistance or current): '))
    
    # Realiza o cálculo conforme a operação escolhida
    if operation2 == 'R':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)  # Calculando a resistência
    elif operation2 == 'C':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)  # Calculando a corrente
    elif operation2 == 'P':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)  # Calculando a potência
    elif operation2 == 'T':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)  # Calculando a tensão
    else:
        print('You have not typed a valid operator, please run the program again.')

# Função para conversão de unidades de potência e corrente
def calculate3():
    # Solicita ao usuário a operação de conversão
    operation3 = input(''' 
    Avanço de sistemas elétricos!! 
    Converter Watt para Kilowatt kW = W / 1000
    Converter Kilowatt para Watt W = kW * 1000
    Converter Watt para Megawatt MW = W / 1000000
    Converter Megawatt para Watt W = MW * 1000000
    Converter miliampere para ampere A = mA / 1000
    Converter miliampere para ampere mA = A * 1000
    ''')

    # Solicita o número para a conversão
    number = float(input('Please enter the number: '))

    # Realiza a conversão conforme a operação escolhida
    if operation3 == 'KW':
        print('{} / 1000 = '.format(number))
        print(number / 1000)  # Conversão de Watt para Kilowatt
    elif operation3 == 'W':
        print('{} * 1000 = '.format(number))
        print(number * 1000)  # Conversão de Kilowatt para Watt
    elif operation3 == 'MW':
        print('{} / 1000000 = '.format(number))
        print(number / 1000000)  # Conversão de Watt para Megawatt
    elif operation3 == 'MWW':
        print('{} * 1000000 = '.format(number))
        print(number * 1000000)  # Conversão de Megawatt para Watt
    elif operation3 == 'A':
        print('{} / 1000 = '.format(number))
        print(number / 1000)  # Conversão de miliampere para ampere
    elif operation3 == 'MA':
        print('{} * 1000 = '.format(number))
        print(number * 1000)  # Conversão de ampere para miliampere
    else:
        print('You have not typed a valid operator, please run the program again.')

# Função que permite ao usuário calcular novamente ou sair
def again():
    calc_again = input(''' 
    Do you want to calculate again? 
    Please type Y for YES or N for NO. 
    ''')

    # Verifica a escolha do usuário
    if calc_again.upper() == 'Y':
        calculate()  # Chama a função de cálculo novamente
    elif calc_again.upper() == 'N':
        print('See you later.')  # Encerra o programa
    else:
        print("Invalid input. Please type Y or N.")
        again()  # Repete a solicitação caso a entrada seja inválida

# Chama a função de cálculo inicial
calculate()

# Após o cálculo, o programa pergunta se o usuário deseja calcular novamente
again()
