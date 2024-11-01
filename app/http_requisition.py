"""Essa será a Classe Requisition HTTP"""

import httpx
import logging
import asyncio
from app.utils import *

logging.basicConfig(level=logging.INFO)


class Requisition:
    def __init__(self):
        self.url = None
        self.year = None
        self.area = None
        self.subarea = None

    async def get_requisition(self, url):
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

    def create_url_link(self, year, area, subarea=None):
        year, area, subarea = transform_input_into_string(
            year=year, area=area, subarea=subarea
        )

        if not subarea:
            url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={str(year)}&opcao={area}"
            self.url = url
            return self.url

        else:
            url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao={subarea}&ano={year}&opcao={area}"
            self.url = url
            return self.url
