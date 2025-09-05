import random
import os
import sys
import time
import webbrowser

def abrir_janelas():
    url = [
        "https://www.youtube.com",
        "https://www.google.com",
        "https://www.wikipedia.org",
        "https://www.pr.senac.br",
        "https://www.linkedin.com",
    ]

    for i in url:
        webbrowser.open(i)
def jogar():
    opcoes = 6
    escolhido = random.randint(1, opcoes)

    escolha = int(input(f"Escolha um numero entre 1 e {opcoes}"))
    if escolha == escolhido:
        print("bye bye, seu PC será deligado! 👻")
        abrir_janelas()
        time.sleep(5)
        if sys.platform == 'win32':
            os.system("shutdown /s /t 1")
        elif sys.platform == 'linux' or sys.platform == 'linux2':
            os.system("shutdown now")
        elif sys.platform == 'darwin':
            os.system("sudo shutdown -h now")
    else:
        print("você está seguro, por enquanto! 😁")

def regras():
    print("""
    Regras do Jogo:
    1. Escolha um número entre 1 e 6.
    2. Se você acertar o número sorteado, seu computador será desligado.
    3. Se você errar, estará seguro... por enquanto!
    """)

def menu_principal():
    print("Menu Principal")
    print("1. iniciar jogo")
    print("2. ver regras")
    print("3. sair")

    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        jogar()
    elif escolha == 2:
        regras()
    elif escolha == 3:
        sair()
    else:
        print("Opção inválida.")
menu_principal()