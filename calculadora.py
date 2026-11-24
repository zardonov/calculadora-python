print("Minha calculadora")
print("")

while True:
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "0":
        print("Saindo da calculadora...")
        break

    if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
        try:
            n1 = float(input("Digite o primeiro numero: "))
            n2 = float(input("Digite o segundo numero: "))
        except ValueError:
            print("Digite um numero valido.")
            print("")
            continue

        if opcao == "1":
            resultado = n1 + n2
            print("Resultado:", resultado)

        elif opcao == "2":
            resultado = n1 - n2
            print("Resultado:", resultado)

        elif opcao == "3":
            resultado = n1 * n2
            print("Resultado:", resultado)

        elif opcao == "4":
            if n2 == 0:
                print("Nao da para dividir por zero.")
            else:
                resultado = n1 / n2
                print("Resultado:", resultado)
    else:
        print("Opcao invalida.")

    print("")
