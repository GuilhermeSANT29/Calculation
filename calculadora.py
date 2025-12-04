# Função de menu para a calculadora
def menu_calculadora():
    while True:
        print("\n--- Menu da Calculadora ---")
        print("1. Binário para Decimal")
        print("2. Decimal para Binário")
        print("3. Decimal para Hexadecimal")
        print("4. Hexadecimal para Decimal")
        print("5. Binário para Hexadecimal")
        print("6. Operações Aritméticas entre Binários")
        print("7. Sair")


        opcao = int(input("\nEscolha a opção (1-7): "))


        if opcao == 1:
            # Conversão de Binário para Decimal
            binario = input("Digite o número binário: ")
            try:
                decimal = int(binario, 2)
                print(f"O número binário {binario} em decimal é: {decimal}")
            except ValueError:
                print("Valor inválido. Certifique-se de que o número binário está correto.")


        elif opcao == 2:
            # Conversão de Decimal para Binário
            numeroDecimal = int(input("Digite seu número decimal: "))
            binario = bin(numeroDecimal)[2:]  # Remove o prefixo '0b'
            print(f"O número {numeroDecimal} em binário é: {binario}")


        elif opcao == 3:
            # Conversão de Decimal para Hexadecimal
            numeroDecimal = int(input("Digite seu número decimal: "))
            hexadecimal = hex(numeroDecimal)[2:].upper()  # Remove o prefixo '0x' e converte para maiúsculo
            print(f"O número {numeroDecimal} em hexadecimal é: {hexadecimal}")


        elif opcao == 4:
            # Conversão de Hexadecimal para Decimal
            hexadecimal = input("Digite o número hexadecimal: ")
            try:
                decimal = int(hexadecimal, 16)
                print(f"O número hexadecimal {hexadecimal} em decimal é: {decimal}")
            except ValueError:
                print("Valor inválido. Certifique-se de que o número hexadecimal está correto.")


        elif opcao == 5:
            # Conversão de Binário para Hexadecimal
            binario = input("Digite o número binário: ")
            try:
                decimal = int(binario, 2)
                hexadecimal = hex(decimal)[2:].upper()  # Converte para hexadecimal
                print(f"O número binário {binario} em hexadecimal é: {hexadecimal}")
            except ValueError:
                print("Valor inválido. Certifique-se de que o número binário está correto.")


        elif opcao == 6:
            # Operações Aritméticas entre Binários
            bin1 = input("Digite o primeiro número binário: ")
            bin2 = input("Digite o segundo número binário: ")
            op = input("Escolha a operação (+, -, *, /): ")


            try:
                num1 = int(bin1, 2)
                num2 = int(bin2, 2)


                if op == '+':
                    resultado = num1 + num2
                elif op == '-':
                    resultado = num1 - num2
                elif op == '*':
                    resultado = num1 * num2
                elif op == '/':
                    if num2 == 0:
                        print("Erro: Divisão por zero!")
                        continue
                    resultado = num1 // num2  # Divisão inteira (arredonda para baixo)
                else:
                    print("Operação inválida!")
                    continue


                # Exibe o resultado em binário
                print(f"O resultado de {bin1} {op} {bin2} é: {bin(resultado)[2:]}")
            except ValueError:
                print("Valor inválido. Certifique-se de que os números binários estão corretos.")


        elif opcao == 7:
            print("Saindo da calculadora.")
            break


        else:
            print("Opção inválida! Escolha uma opção válida entre 1 e 7.")


# Chama a função do menu
menu_calculadora()