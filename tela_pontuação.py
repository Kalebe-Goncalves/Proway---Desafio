from tkinter import *
from datetime import datetime
from main import retornar_valores_bd

"""
Aplicação em Python utilizando Tkinter para a criação da Interface Grafíca para o Usuário, onde será exibida a pontuação da temporada
"""


class AppDesafio_Pontuacao(object):
    """
    Classe responsável pelos métodos e parâmetros da Janela pai
    """

    def __init__(self):

        self.master = Tk()
        self.lista = []
        self.master.title("Registro Pontuações Maria")
        self.master.resizable(0, 0)

        self.valor1 = Label(self.master, text="Jogo")
        self.valor1["font"] = ("Arial", "14", "bold")
        self.valor1["width"] = 5
        self.valor1["padx"] = 5
        self.valor1.grid(row=2, column=0)

        self.valor2 = Label(self.master, text="Placar")
        self.valor2["font"] = ("Arial", "14", "bold")
        self.valor2["width"] = 5
        self.valor2.grid(row=2, column=1)

        self.valor3 = Label(self.master, text="Min."+"\n"+"Temporada")
        self.valor3["font"] = ("Arial", "14", "bold")
        self.valor3["width"] = 10
        self.valor3.grid(row=2, column=2)

        self.valor4 = Label(self.master, text="Max."+"\n"+" Temporada")
        self.valor4["font"] = ("Arial", "14", "bold")
        self.valor4["width"] = 10
        self.valor4.grid(row=2, column=3)

        self.valor5 = Label(self.master, text="Quebra" +
                            "\n"+" Recorde"+"\n"+" Min.")
        self.valor5["font"] = ("Arial", "14", "bold")
        self.valor5["width"] = 15
        self.valor5.grid(row=2, column=4)

        self.valor6 = Label(self.master, text="Quebra" +
                            "\n"+" Recorde"+"\n"+" Max.")
        self.valor6["font"] = ("Arial", "14", "bold")
        self.valor6["width"] = 15
        self.valor6.grid(row=2, column=5)

        self.pontuacoes_lista = retornar_valores_bd()

        linha = 5
        # Lógica responsável por ler os valores e posiciona-los corretamente em cada campo
        for coluna_dado in self.pontuacoes_lista:
            texto = str(coluna_dado.num_partida)
            self.conteudo = Label(self.master, text=texto, font=(
                "Arial", "12"), width=5, pady=10)
            self.conteudo.grid(row=linha, column=0)
            texto = str(coluna_dado.placar)
            self.conteudo = Label(self.master, text=texto,
                                  font=("Arial", "12"), width=5)
            self.conteudo.grid(row=linha, column=1)
            texto = str(coluna_dado.minimo)
            self.conteudo = Label(self.master, text=texto,
                                  font=("Arial", "12"), width=10)
            self.conteudo.grid(row=linha, column=2)
            texto = str(coluna_dado.maximo)
            self.conteudo = Label(self.master, text=texto,
                                  font=("Arial", "12"), width=10)
            self.conteudo.grid(row=linha, column=3)
            texto = str(coluna_dado.recorde_min)
            self.conteudo = Label(self.master, text=texto,
                                  font=("Arial", "12"), width=15)
            self.conteudo.grid(row=linha, column=4)
            texto = str(coluna_dado.recorde_max)
            self.conteudo = Label(self.master, text=texto,
                                  font=("Arial", "12"), width=15)
            self.conteudo.grid(row=linha, column=5)
            self.conteudo = None
            linha += 1

        self.master.mainloop()


if __name__ == "__main__":
    AppDesafio_Pontuacao()
