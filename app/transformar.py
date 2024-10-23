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

from json import load
from bs4 import BeautifulSoup
import pandas as pd


from app.models import *
from app.requisicao_http import Requisition


class Transform(Requisition):

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

    async def get_dados(self, url):
        response = await super().requisicao_get(url)
        return response

    def formatar_dados(self, response):
        soup = BeautifulSoup(response, "html.parser")
        soup = soup.find("thead").parent
        # df = pd.DataFrame()
        headers = ["category"]
        # Inicializa uma lista para armazenar os resultados
        tds_em_trs = []
        df = pd.DataFrame()
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

    async def consultar_todo_periodo(self, area, subarea=None):
        ############################# AQUI TEM QUE AJUSTAR O PERÌODO PARA 2023 ##################################
        lista_de_periodos = [i for i in range(1970, 1972)]
        ################################################# AJUSTAR ###############################################

        urls = [
            self.criar_link(ano=ano, area=area, subarea=subarea)
            for ano in lista_de_periodos
        ]
        response = {}

        for ano, url in zip(lista_de_periodos, urls):
            data = await self.get_dados(url=url)
            if data is None:
                print(f"Dados não encontrados para o ano {ano}. URL: {url}")
                continue  # Pula para o próximo ano se não houver dados
            data = self.formatar_dados(data)

            response[f"{ano}"] = data

        return response

    async def consultar_todas_as_areas(self, area, SubModel):
        data = []

        for subarea in SubModel:
            response = await self.consultar_todo_periodo(
                area=area, subarea=subarea.name
            )
            data[f"{subarea.name}"] = response
            # data.append(response)
        return data
