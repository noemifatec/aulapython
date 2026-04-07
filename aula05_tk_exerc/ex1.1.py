from tkinter import *
tela = Tk()

tela.title("Fatec Registro")
tela.geometry("400x250")

lbl_nome = Label(tela, text="Digite o nome:")
lbl_nome.grid(row=0, column=0, padx=10, pady=5)
ent_nome = Entry(tela)
ent_nome.grid(row=0, column=1, padx=10, pady=10)

lbl_email = Label(tela, text="Digite o email:")
lbl_email.grid(row=1, column=0, padx=10, pady=10)
ent_email = Entry(tela)
ent_email.grid(row=1, column=1, padx=10, pady=10)

lbl_nome = Label(tela, text="Digite o telefone:")
lbl_nome.grid(row=3, column=0, padx=10, pady=10)
ent_nome = Entry(tela)
ent_nome.grid(row=3, column=1, padx=10, pady=10)

lbl_nome = Label(tela, text="Digite o endereço:")
lbl_nome.grid(row=4, column=0, padx=10, pady=10)
ent_nome = Entry(tela)
ent_nome.grid(row=4, column=1, padx=10, pady=10)





btn_enviar = Button(tela, text="Cadastrar Cliente")
btn_enviar.grid(row=9, column=0, columnspan=2, pady=10)



tela.mainloop()