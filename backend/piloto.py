print("ola mundo")

def maior(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    elif num1 == num2:
        return "os numeros são iguais!"
    else:
        return "Eventos inesperados"


#Entrada de dados
num1 = int(input("insira o primeiro número: "))
num2 = int(input("insira o segundo número: "))

resultado = maior(num1, num2)
print("O maior número é ", resultado)