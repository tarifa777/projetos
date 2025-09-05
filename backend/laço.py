import random

#lista
#              0          1            2         3       4
salgados = ["Risoles", "Cola cola", "Coxinha", "kibe", "Suco",
             "Bolo", "mini-churros", "Pão de mel", "Donuts", "Cachorro-quente"]

print(salgados[2]) #coxinha
print("O sorteado foi: ", random.choices(salgados))

#imprimindo todos salgados
#imprima no intervalo do tamanho(len) da lista de salgados
for posicao in range(len(salgados)):
    print(posicao, " - ", salgados[posicao])

contador = 0
while contador < 19:
    print("O Tarifa")
    contador = contador + 1

def listar():
    for posicao in range(len(salgados)):
        print(posicao, " - ", salgados[posicao])

opcao = 0
while opcao != 3:
        opcao = int (input("insira a opcao: "))

        if opcao == 1:
            #efetuando entrada de dados na lista
            item = input("digete um item para adicionar na lista ")
            salgados.append(item)
            listar()

            
        if opcao == 2:
            #efetuando entrada de dados na lista
            item = input("digete um item para excluir: ")
            salgados.remove(item)
            listar()
        if opcao == 4:
            listar()
        if opcao == 5:
            break


