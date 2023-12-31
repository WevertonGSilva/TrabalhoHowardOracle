from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_carrinhos = config.QUERY_COUNT.format(tabela="carrinhos")
        self.qry_total_produtos = config.QUERY_COUNT.format(tabela="produtoss")
        self.qry_total_itensCarrinhos = config.QUERY_COUNT.format(tabela="itensCarrinhos")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Weverton Gomes da Silva, Diogo Rocha da Silva Pelanda, Ronaldo Luiz de Almeida Junior, Taciane da Silva Santos, João Pedro Xavier Peccini, Arianne Geremias Batista, Mayra Lazarone Barros "
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_total_carrinhos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_carrinhos)["total_carrinhos"].values[0]

    def get_total_produtos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_produtos)["total_produtoss"].values[0]

    def get_total_itensCarrinhos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_itensCarrinhos)["total_itenscarrinhos"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE CARRINHO DE COMPRAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - CARRINHOS:         {str(self.get_total_carrinhos()).rjust(5)}
        #      2 - PRODUTOS:     {str(self.get_total_produtos()).rjust(5)}
        #      3 - ITENSCARRINHOS:          {str(self.get_total_itensCarrinhos()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}

        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """