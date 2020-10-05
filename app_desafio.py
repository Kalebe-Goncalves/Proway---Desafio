from tkinter import *
from PIL import ImageTk, Image
import tela_inserir_dados
import tela_pontuação
from main import exportar_planilha_excel

"""
Aplicação em Python utilizando Tkinter para a criação da Interface Grafíca para o Usuário
"""


class AppDesafio_Home(object):
    """
    Classe responsável pelos métodos e parâmetros da Janela pai
    """

    def __init__(self):
        """
        Inicialização da classe
        """

        self.master = Tk()  # Raiz da Janela
        self.jan = None     # Váriavel que verifica a existência de uma janela filha
        # Determina o título da Janela
        self.master.title("Registro Pontuações Maria")
        self.image = ImageTk.PhotoImage(Image.open(
            "img_fundo.jpg"))   # Leitura do caminho da imagem
        self.w = self.image.width()     # retorna largura da imagem
        self.h = self.image.height()    # retorna altura da imagem
        # determina o tamanho da janela de forma geométrica
        self.master.geometry('%dx%d+0+0' % (self.w, self.h))
        # determina que a tela não pode ser expandida ou diminuida
        self.master.resizable(0, 0)
        # cria uma Label onde é colocada a imagem
        self.background_label = Label(self.master, image=self.image)
        # determina a posição da Label que contêm a imagem e a escala da imagem
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.titulo = Label(
            self.master, text="Registro de Pontuações", width=20)   # Label contendo o título do App
        # Determina a formatação da escrita da Label do título
        self.titulo["font"] = ("Arial", "19", "bold")
        # posicionamento da Label do título
        self.titulo.grid(row=0, column=0, pady=20)

        # Determina o Botão posicionado na raiz da Janela e o texto do botão
        self.button1 = Button(self.master, text="Inserir")
        self.button1["font"] = ("Arial", "16")
        self.button1["width"] = 25      # Define o comprimento da widget
        self.button1["command"] = self.inserir_dados  # Define a ação da widget
        self.button1.grid(row=2, column=0)

        self.button2 = Button(self.master, text="Acompanhar Resultados")
        self.button2["font"] = ("Arial", "16")
        self.button2["width"] = 25
        self.button2["command"] = self.abrir_tabela
        self.button2.grid(row=3, column=0)

        self.button2 = Button(self.master, text="Acompanhar Resultados - Xml")
        self.button2["font"] = ("Arial", "16")
        self.button2["width"] = 25
        self.button2["command"] = self.abrir_tabela_xml
        self.button2.grid(row=4, column=0)

        self.button3 = Button(self.master)
        self.button3["text"] = "Sair"
        self.button3["font"] = ("Arial", "16")
        self.button3["width"] = 25
        self.button3["command"] = self.Sair
        self.button3.grid(row=5, column=0)

        self.master.mainloop()      # Loop da aplicação na raiz da janela que contêm as widgets

    def inserir_dados(self):
        """
        Método que inicializa uma Janela filha (em cima da raiz principal) onde é possível a interação do Usuário para inserir novos dados.
        """
        if self.jan is None:    # Verifica a existência de uma Janela filha
            # Inicializa a Classe responsável por criar a Janela filha
            self.jan = tela_inserir_dados.AppDesafio_Inserir()
            self.jan.master.lift()      # Define foco na Janela filha
            # Define a ação de fechar a Janela filha
            self.jan.master.protocol("WM_DELETE_WINDOW", self.Sair_jan)
        else:
            self.jan.master.lift()

    def abrir_tabela(self):
        """
        Método que inicializa uma Janela filha (em cima da raiz principal) onde é possível a leitura dos dados (Pontuações) contidas no banco de dados.
        """
        if self.jan is None:
            self.jan = tela_pontuação.AppDesafio_Pontuacao()
            self.jan.master.lift()
            self.jan.master.protocol("WM_DELETE_WINDOW", self.Sair_jan)
        else:
            self.jan.master.lift()

    def abrir_tabela_xml(self):
        """
        Método responsável por iniciar as alterações na planilha através do comando do usuário (apertar o botão - button2)
        """
        exportar_planilha_excel()   # Executa as alterações na planilha

    def Sair(self):
        """
        Método responsável por fechar e destruir a Janela pai
        """
        self.master.destroy()   # destroí a raiz da janela

    def Sair_jan(self):
        """
        Método responsável por fechar e destruir a Janela filha
        """
        self.jan.destroy()
        self.jan = None


if __name__ == "__main__":
    AppDesafio_Home()
