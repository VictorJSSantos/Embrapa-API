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

from utils.basemodel import *
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
        response = super().requisicao_get(url)
        return response

    def formatar_dados(self, response):
        soup = BeautifulSoup(response, "html.parser")
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

        # print(len(df.columns))

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

        return df

    def consultar_todo_periodo(self, area, subarea=None):
        lista_de_periodos = [i for i in range(1970, 1974)]
        df = None

        for i in lista_de_periodos:
            url = self.criar_link(
                ano=i, area=area, subarea=subarea
            )  # Criar a URL para cada ano (o que muda a URL)

            # Preparação dos dados para criação do DataFrame
            data = self.get_dados(url=url)
            data = self.formatar_dados(data)
            data["Ano"] = i
            # data["Area"] = area

            if df is None:
                df = pd.DataFrame(data)
            else:
                df = pd.concat(
                    [df, pd.DataFrame(data)], ignore_index=True
                )  # Concatenação dos resultados ao DataFrame com todos os dados

        json = df.to_dict(
            orient="dict"
        )  # Transformação em JSON final após o loop para não quebrar a API
        return json

    def consultar_todas_as_areas(self, area, Model):
        lista_de_subareas = [submodel.name for submodel in Model]
        df = None
        for subarea in lista_de_subareas:
            data = self.consultar_todo_periodo(area=area, subarea=subarea)
            data = pd.DataFrame.from_dict(data)
            data["Subarea"] = Model[subarea].value

            if df is None:
                df = pd.DataFrame(data)
            else:
                df = pd.concat(
                    [df, pd.DataFrame(data)], ignore_index=True
                )  # Concatenação dos resultados ao DataFrame com todos os dados

        json = df.to_dict(
            orient="dict"
        )  # Transformação em JSON final após o loop para não quebrar a API
        return json
