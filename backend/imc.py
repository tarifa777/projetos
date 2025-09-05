peso = float(input("insira o peso:(kg): "))
altura = float(input("insira a altura:(metros): "))

imc = peso / (altura * altura)
print("meu imc e ", imc)

if (imc < 18.05):
    print("abaixo do peso")
elif (imc <= 24.09):
    print("peso normal")
elif (imc <= 32.39):
    print("sobrepeso")
elif (imc <= 34.09):
    print("obesidade grau 1")
elif (imc <= 39.39):
    print("voce esta com obesidade grau 2 ")                  
