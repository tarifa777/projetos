#entrada de dados
nota1 = float(input("Insira a primeira nota"))
nota2 = float(input("Insira a segunda nota"))
nota3 = float(input("Insira a terceira nota"))
nota4 = float(input("Insira a quarta nota"))

#processamento de dados
notaFinal = (nota1 + nota2 + nota3 + nota4) / 4

#saida
print("A nota final é ", notaFinal)

if notaFinal < 60:
    print("o aluno está reprovado!")
elif(notaFinal <= 70):
    print("o aluno foi mediano")
elif(notaFinal <= 80):
    print("o aluno foi muito bom")
else:
    print("o aluno foi excelente! ")