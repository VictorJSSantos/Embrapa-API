""" Aqui será onde será criada a classe para o Extrator de Dados do site
Coisas que ele precisa fazer são:
variáveis:
como é classe, self (para poder instanciar numa variável), ano, area e subarea

métodos: 
validar ano, validar area, validar subarea
adicionar a registros para salvar, criar um dataframe com resultados

Vai encapsular a cls Requisition para poder fazer a requisição a 
partir daqui e sobrescrever suas funcionalidades

"""

from utils.extrair import Requisition
from json import load
from bs4 import BeautifulSoup
import pandas as pd


class Extractor(Requisition):

    def __init__(self):
        super().__init__()
        self.ano = None
        self.area = None
        self.subarea = None
        self.url = None

    def adicionar_coluna(self, coluna):
        self.columns = coluna

    def adicionar_dados(self, dados):
        self.dados.append(dados)

    def limpar_lista(self):
        self.dados.clear()

    def get_dados(self, url):
        data = super().requisicao_get(url)
        return data

    def formatar_dados(self, data):
        soup = BeautifulSoup(data, "html.parser")
        soup = soup.find("thead").parent
        headers = ["category"]
        # Inicializa uma lista para armazenar os resultados
        tds_em_trs = []
        # Inicializando a lista de categorias
        category = []

        # Itera sobre as linhas da tabela
        for tr in soup.find_all("tr"):
            # Para cada linha, extrai o texto de cada célula (td)
            tds = tr.find_all("td")

            # Verifica se a linha é um tb_item e extrai a categoria
            if "tb_item" in (td.get("class", [None])[0] for td in tds):
                tb_item = tds[0].text.strip()  # Remove espaços e quebras de linha
                category.append(tb_item)

            # Adiciona o resultado como um array de 3 elementos (ou quantos td's houver)
            tds_formatados = [
                td.text.strip().replace("\n", "") for td in tds
            ]  # Formata cada td

            tds_em_trs.append(tds_formatados)

            df = pd.DataFrame(tds_em_trs)

        print(len(df.columns))

        if len(headers) == 2:
            tds_em_trs.append(
                tds_formatados + [category[-1] if category else None]
            )  # Adiciona a categoria
            # Converte a lista para um DataFrame
            df = pd.DataFrame(
                tds_em_trs, columns=["Produto", "Quantidade (L.)", "item_class"]
            )

        if len(headers) == 3:
            df = pd.DataFrame(
                tds_em_trs, columns=["País", "Quantidade (L.)", "Valor (US$)"]
            )

        # df = df[1:]
        # df["Ano"] = data["ano"]
        # df["area"] = data["area"]
        # df["subarea"] = data["subarea"]

        return df
