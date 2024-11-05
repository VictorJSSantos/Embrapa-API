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

from bs4 import BeautifulSoup
import pandas as pd


from app.models import *


class TransformRequisition:

    def __init__(self):
        from app.http_requisition import Requisition

        self.requisition = Requisition()
        self.year = None
        self.area = None
        self.subarea = None
        self.url = None

    def add_column(self, column):
        self.columns = column

    async def get_data(self, url):
        response = await self.requisition.get_requisition(url)
        return response

    def format_data(self, response):
        soup = BeautifulSoup(response, "html.parser")
        soup = soup.find("thead").parent
        headers = [th.text.strip() for th in soup.find_all("th")]
        # Inicializa uma lista para armazenar os resultados
        data_by_row_to_list = []
        df = pd.DataFrame()

        # Itera sobre as linhas da tabela
        for tr in soup.find_all("tr"):
            # Para cada linha, extrai o texto de cada célula (td)
            tds = tr.find_all("td")

            # Adiciona o resultado como um array de elementos
            row_value_list = [
                td.text.strip().replace("\n", "") for td in tds
            ]  # Formata cada td

            data_by_row_to_list.append(row_value_list)

        df = pd.DataFrame(data_by_row_to_list, columns=headers)

        return df.to_dict(orient="dict")

    async def get_all_data(self, area, subarea=None):
        ############################# AQUI TEM QUE AJUSTAR O PERÌODO PARA 2023 ##################################
        period_list = [i for i in range(1970, 2022)]
        ################################################# AJUSTAR ###############################################

        urls = [
            self.requisition.create_url_link(year=year, area=area, subarea=subarea)
            for year in period_list
        ]
        response = {}

        for year, url in zip(period_list, urls):
            data = await self.get_data(url=url)
            if data is None:
                print(f"Dados não encontrados para o ano {year}. URL: {url}")
                continue  # Pula para o próximo ano se não houver dados
            data = self.format_data(data)

            response[f"{year}"] = data

        return response

    async def get_data_from_all_areas(self, area, SubModel):
        data = {}

        for subarea in SubModel:
            response = await self.get_all_data(area=area, subarea=subarea.name)
            data[f"{subarea.value}"] = response
        return data
