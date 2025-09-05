#importação de biblioteca que manipula janelas
import tkinter as tk
from tkinter import messagebox
#importação de biblioteca de sorteio
import random
#importação de biblioteca que manipula o navegador
import webbrowser
#importação de biblioteca que manipula o computador
import os
#importação que verifica o tipo de s.o
import sys
#importação de biblioteca que manipula tempo
import time

#criando lista de sites
urls = [
    "https://www.youtube.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.pr.senac.br",
    "https://www.linkedin.com",
]
#função para abrir navegador
def abrir_navegador():
    for url in urls:
        webbrowser.open(url)
        time.sleep(2)
def jogar():
    #sorteia um numero aleatorio de 1 a 6
    numero = random.randint(1, 6)
    sorteado = 5
    
    def verificar_escolha(numero):
        if numero == sorteado:
            messagebox.showinfo("Vixi", "Você perdeu! Seu computador será desligado.")
            abrir_navegador()
            root.destroy()
            if sys.platform == "win32":
                os.system("shutdown /s /t 1")
            elif sys.platform == 'linux':
                    os.system("shutdown now")
            elif sys.platform == "darwin":
                    os.system("sudo shutdown -h now")
        else:
            messagebox.showinfo("Ufa!", "Você ganhou! Por enquanto está seguro.")
            jogar()
    janela = tk.Toplevel()
    janela.title("Escolha um número")
    tk.Label(janela, text="Escolha um número de 1 a 6:").pack(pady=10)
    for i in range(1, 7):
        tk.Button(janela, text=str(i), 
        width=10, command=lambda i=i: [janela.destroy(), verificar_escolha(i)]).pack(pady=10) 

    #inicio janela principal de menu
root = tk.Tk()
root.title("jogo do sorteio")
#define altura e largura da janela
root.geometry("500x500")
tk.Label(root, text="Bem-vindo ao Jogo do Sorteio!", font=("Arial", 14)).pack(pady=15)
#botões do menu
tk.Button(root, text="Jogar", width=20, command=jogar,).pack(pady=10)
tk.Button(root, text="Regras", width=20, command=jogar).pack(pady=10)
tk.Button(root, text="Sair", width=20, command=jogar).pack(pady=10)
                  
root.mainloop()