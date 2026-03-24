from tkinter import *

class Aplicacao:
  def__init__(self):
      self.tela = TK()
       self.configurar_tela()
       self.criar_componentes()

    def configurar_tela(self):
           self.tela.title("Aplicação O_O")
           self.tela.configure(background="#1e3743")
       
    largura = 800
    altura = 300

