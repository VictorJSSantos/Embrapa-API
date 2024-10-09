"""Essa será a Classe Requisition HTTP"""

import requests
from http import HTTPStatus


class Requisition:
    def __init__(self):  # , ano, area, subarea, url
        self.url = None
        self.ano = None
        self.area = None
        self.subarea = None

    def requisicao_get(self, url):
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers)

        if response.status_code == HTTPStatus.OK:
            return response.text
        else:
            return f"Erro ao acessar a página: {response.status_code}"

    def criar_link(self, ano, area, subarea=None):
        if not subarea:
            # print("caso 1 - sem subarea")
            url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao={area}"
            self.url = url
            return self.url

        else:
            # print("caso 2 - COM subarea")
            url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao={subarea}&ano={ano}&opcao={area}"
            self.url = url
            return self.url
