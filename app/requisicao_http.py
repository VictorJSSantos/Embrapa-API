"""Essa será a Classe Requisition HTTP"""

import httpx
import logging
import asyncio
from app.utils import *

logging.basicConfig(level=logging.INFO)


class Requisition:
    def __init__(self):
        self.url = None
        self.ano = None
        self.area = None
        self.subarea = None

    async def requisicao_get(self, url):
        async with httpx.AsyncClient() as client:
            for attempt in range(2):  # Tentar até 3 vezes
                try:
                    logging.info(f"Requisitando URL: {url} - Tentativa {attempt}")
                    response = await client.get(url, timeout=10)
                    response.raise_for_status()
                    return response.text
                except httpx.ConnectError as e:
                    logging.error(f"Erro de conexão: {e}")
                    if (
                        attempt < 2
                    ):  # Se não for a última tentativa, aguardar antes de tentar novamente
                        await asyncio.sleep(2)
                    continue
                except httpx.HTTPStatusError as e:
                    logging.error(f"Erro de status HTTP: {e}")
                    return None
                except Exception as e:
                    logging.error(f"Erro inesperado: {e}")
                    return None

    def criar_link(self, ano, area, subarea=None):
        ano, area, subarea = transformar_dados_de_url_em_string(
            ano=ano, area=area, subarea=subarea
        )

        if not subarea:
            url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={str(ano)}&opcao={area}"
            self.url = url
            return self.url

        else:
            url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao={subarea}&ano={ano}&opcao={area}"
            self.url = url
            return self.url
