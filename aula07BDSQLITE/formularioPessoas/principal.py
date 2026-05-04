from pessoas import ControlePessoas
from PIL import Image, ImageTk
class Principal:
    @staticmethod
    def main():
        #instanciar classe 
        p = ControlePessoas()
        p.executar()
        

if __name__ == "__main__":
    Principal.main()