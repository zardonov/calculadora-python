def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")


def calcular(opcao, numero1, numero2):
    if opcao == "1":
        return numero1 + numero2
    elif opcao == "2":
        return numero1 - numero2
    elif opcao == "3":
        return numero1 * numero2
    elif opcao == "4":
        if numero2 == 0:
            return None
        return numero1 / numero2


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Obrigado por usar a calculadora!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida. Tente novamente.")
            continue

        try:
            numero1 = float(input("Digite o primeiro número: ").replace(",", "."))
            numero2 = float(input("Digite o segundo número: ").replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

        resultado = calcular(opcao, numero1, numero2)

        if resultado is None:
            print("Não é possível dividir por zero.")
        else:
            print(f"Resultado: {resultado:g}")


if __name__ == "__main__":
    main()
