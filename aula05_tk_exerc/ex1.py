from tkinter import *
tela = Tk()

tela.title("Fatec Registro")
tela.geometry("300x200")
lbl_nome = Label(tela, text="Digite o nome:")
lbl_nome.pack(pady=5)
ent_nome = Entry(tela)
ent_nome.pack(pady=5)

lbl_nome = Label(tela, text="Digite o e-mail:")
lbl_nome.pack(pady=5)
ent_nome = Entry(tela)
ent_nome.pack(pady=5)

lbl_nome = Label(tela, text="Digite o telefone:")
lbl_nome.grid(row=0, column=0, padx=10, pady=10)
ent_nome = Entry(tela)
ent_nome.grid(row=0, column=1, padx=10, pady=10)

lbl_nome = Label(tela, text="Digite o endereço:")
lbl_nome.pack(pady=5)
ent_nome = Entry(tela)
ent_nome.pack(pady=5)

btn_enviar = Button(tela, text="Cadastrar Cliente")
btn_enviar.pack(pady=10)



tela.mainloop()
