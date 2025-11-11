import customtkinter as ctk
import sqlite3

janela = ctk.CTk()
janela.title("Calculadora")
janela.geometry("250x500")
ctk.set_appearance_mode("dark")
janela.resizable(False, False)

prompt = ctk.CTkLabel(janela, text="", width=200, height=50, corner_radius=20, fg_color="#1E3A8A")
prompt.place(x=25, y=20)

botoes = [
    ["1",40,80], ["2",100,80], ["3",160,80],
    ["4",40,140], ["5",100,140], ["6",160,140],
    ["7",40,200], ["8",100,200], ["9",160,200],
    ["/",40,260], ["0",100,260], ["-",160,260],
    ["*",40,320], ["+",100,320]
]

def resultar():
    captar = prompt.cget("text")
    prompt.configure(text=eval(captar))
botao_res = ctk.CTkButton(janela, text="=", width=50, height=50, corner_radius=20, fg_color="blue", command=resultar)
botao_res.place(x=160, y=320)

def limpar():
    prompt.configure(text="")
botao_limpar = ctk.CTkButton(janela, text="Limpar", width=170, height=50, corner_radius=20, fg_color="red", command=limpar)
botao_limpar.place(x=40, y=380)

def adicionar_texto(texto):
    antigo = prompt.cget("text")
    prompt.configure(text=antigo+texto)

textinho = ctk.CTkLabel(janela, text="Feito por Eduardo Antunes", font=("Arial", 13))
textinho.place(x=45, y=450)

for button in botoes:
    botao = ctk.CTkButton(janela, text=button[0], width=50, height=50, corner_radius=20, fg_color="blue", command=lambda n=button[0]: adicionar_texto(n))
    botao.place(x=button[1], y=button[2])

janela.mainloop()