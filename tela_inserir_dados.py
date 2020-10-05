from tkinter import Tk, Frame, Label, Button, Entry, BOTTOM
from tkinter import ttk
from main import inserir_dados, retornar_valores_bd

"""
Aplicação em Python utilizando Tkinter para a criação da Interface Grafíca para o Usuário, onde será exibida a pontuação da temporada
"""


class AppDesafio_Inserir(object):
    """
    Classe responsável pelos métodos e parâmetros da Janela pai
    """

    def __init__(self):

        self.master = Tk()
        self.master.title("Registro Pontuações Maria")
        self.master.resizable(0, 0)

        self.titulo = Label(self.master, text="Placar: ")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo["width"] = 15
        self.titulo.grid(row=1, column=0)

        self.text_partida = Entry(self.master)
        self.text_partida["width"] = 15
        self.text_partida["font"] = ("Arial", "12")
        self.text_partida.grid(row=1, column=1)

        self.button1 = Button(self.master, text="Inserir")
        self.button1["font"] = ("Arial", "12")
        self.button1["width"] = 10
        self.button1["command"] = self.inserir_dados_bd
        self.button1.grid(row=1, column=2)

        self.master.mainloop()

    def inserir_dados_bd(self):
        """
        Método responsável por capturar o valor inserido pelo Usuário e realizar a comunicação com o controle (main.py) para realizar o tratamento correto dos valores.
        """
        placar = int(self.text_partida.get())
        # condição especificada no problema (regra de negócio)
        if placar >= 0 and placar < 1000:
            # condicao que verifica se é a primeira partida inserida
            if len(retornar_valores_bd()) == 0:
                inserir_dados(placar, 0, 0, 0, 0, 0)
            else:
                for dado in retornar_valores_bd():
                    jogo = dado.num_partida
                    minimo = dado.minimo
                    maximo = dado.maximo
                    rec_min = dado.recorde_min
                    rec_max = dado.recorde_max
                inserir_dados(placar, jogo, minimo, maximo, rec_min, rec_max)
        else:   # exibe mensagem de erro ao usuário caso valor for inválido
            msg = "erro valor invalido"
            self.msg = Label(self.master, text=msg,
                             font=("Arial", "12", "italic"))
            self.msg.grid(row=2, column=3)
