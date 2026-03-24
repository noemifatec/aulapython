from tkinter import *
#Criando Tela do Tkinter - Interface Gráfica
tela = Tk()

tela.title("Fatec Registro")

tela.configure(background="#3dd44c")

tela.geometry("700x500")

#redimensionar tela true=habilita/false=desabilita
tela.resizable(True,True)
tela.minsize(width=700, height=600)
tela.maxsize(width=700, height=800)
#Criando label
lbl_texto = Label(tela,text="Digite seu nome: ",bg="red",foreground="#FFF").place(x=10,y=20)

lbl_texto = Label(tela,text="Digite seu telefone: ",bg="#FFF",fg="green", font=("Arial","10","bold italic")).place(x=10,y=40)

#Criando caixa de texto
txt_nome = Entry(tela,width=50, borderwidth=3,bg="#e19374", fg="blue")
txt_nome.place(x=70,y=60)

txt_tel=Entry(tela, width=50, borderwidth= 3, bg ="white", fg="blue")
txt_tel.place(x=160, y=60)
#txt_tel.insert("Coloque aqui o telefone")
def mostradados():
    lbl_mostra = Label (tela, text ="Bem vindo: " + txt_nome.get() + "\ntelefone: "
    txt_tel.get())
    lbl_mostra.place(x=100, y=150)
    #Criando botão 

btn_botao = Button(tela, text="Mostrar dados" , command=mostradados)
btn_botao.place(x=160, y=100)



#Executar Tela
tela.mainloop()