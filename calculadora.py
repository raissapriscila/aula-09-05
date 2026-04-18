import math
import random

# CALCULADORA

def calculadora():
    opcao = ""
    
    while opcao != "0":
        print("\n--- CALCULADORA ---")
        print("1 Soma")
        print("2 Subtração")
        print("3 Multiplicação")
        print("4 Divisão")
        print("5 Tabuada")
        print("6 Fibonacci")
        print("0 Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print("Resultado:", a + b)

        elif opcao == "2":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print("Resultado:", a - b)

        elif opcao == "3":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print("Resultado:", a * b)

        elif opcao == "4":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            if b != 0:
                print("Resultado:", a / b)

        elif opcao == "5":
            n = int(input("Número: "))
            print("\nTabuada:")
            for i in range(1, 11):
                print(n, " * ", i, " = ", n * i)

        elif opcao == "6":
            n = int(input("Quantidade: "))
            a, b = 0, 1
            print("Fibonacci:")
            for i in range(n):
                print(a, end=" ")
                a, b = b, a + b
            print()

