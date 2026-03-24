class Soma_Numeros:
    def criar_componentes(self):

        self.txt_n2 = Entry(self.frame)
        self.txt_n2.grid(row=3, column= 1, pady = 5)
        #Resultado
        Label(self.frame, text="Resultado: ").grid(row =4 , column = 0, sticky="w", pady =2) 
        self.txt_resul.grid(row= 4, column =1, pady = 5)
        #Botão
        self.btn_botao = Button(self.frame, text = "Calcular", command = self.calcular)
        self.btn_botao.grid(row = 5, column = 0, columnspan = 2, pady = 15)
