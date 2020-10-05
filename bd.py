from peewee import Model, CharField, IntegerField, SqliteDatabase, ForeignKeyField

"""
Código desenvolvido com o objetivo de inicializar e especificar as características do banco de dados
"""


arq = 'pontuacao_basqueteMaria.db'
bd = SqliteDatabase(arq)


class BaseModel(Model):
    """
    Modelo herdado da biblioteca, necessário para a criação da tabela
    """
    class Meta:
        database = bd


class Partida(BaseModel):
    """
    Classe onde é definido os campos da tabela Partida
    """
    num_partida = IntegerField(null=False)
    placar = IntegerField()
    minimo = IntegerField()
    maximo = IntegerField()
    recorde_min = IntegerField()
    recorde_max = IntegerField()


def main():
    """
    Função que acessa o banco de dados e cria a tabela Partida
    """
    bd.connect()
    bd.create_tables([Partida])


main()
