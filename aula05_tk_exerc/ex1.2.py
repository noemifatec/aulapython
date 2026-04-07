from tkinter import *
from tkinter import messagebox
#Funções
def click():
    nome = ent_nome.get()
    lbl_dados = Label(tela, text = nome, fg="blue", font=("Arial", 10, "bold"))
    lbl_dados.grid(row=5, column=0, columnspan=2, pady=10)

     email = ent_email.get()
    lbl_dados = Label(tela, text = email, fg="blue", font=("Arial", 10, "bold"))
    lbl_dados.grid(row=6, column=0, columnspan=2, pady=10)

tela = Tk()
tela.title("Fatec Registro")
tela.geometry("400x350")

# --- LINHA 0: NOME ---
lbl_nome = Label(tela, text="Digite o nome:")
lbl_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w") # sticky="w" alinha à esquerda (West)
ent_nome = Entry(tela)
ent_nome.grid(row=0, column=1, padx=10, pady=5)

# --- LINHA 1: EMAIL ---
lbl_email = Label(tela, text="Digite o email:")
lbl_email.grid(row=1, column=0, padx=10, pady=5, sticky="w")
ent_email = Entry(tela)
ent_email.grid(row=1, column=1, padx=10, pady=5) # Mesma row do label!

# --- LINHA 2: TELEFONE ---
lbl_tel = Label(tela, text="Digite o telefone:")
lbl_tel.grid(row=2, column=0, padx=10, pady=5, sticky="w")
ent_tel = Entry(tela)
ent_tel.grid(row=2, column=1, padx=10, pady=5) # Mesma row do label!

# --- LINHA 3: ENDEREÇO ---
lbl_end = Label(tela, text="Digite o endereço:")
lbl_end.grid(row=3, column=0, padx=10, pady=5, sticky="w")
ent_end = Entry(tela)
ent_end.grid(row=3, column=1, padx=10, pady=5) # Mesma row do label!


# --- BOTÃO ---
btn_enviar = Button(tela, text="Cadastrar Cliente", command=click)
btn_enviar.grid(row=4, column=0, columnspan=2, pady=20)

tela.mainloop()