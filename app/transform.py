from bs4 import BeautifulSoup


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
        formatted_data = {header: {} for header in headers}

        for row_index, tr in enumerate(soup.find_all("tr")):
            tds = tr.find_all("td")
            for col_index, td in enumerate(tds):
                header = headers[col_index]
                formatted_data[header][str(row_index)] = (
                    td.text.strip().replace("\n", "") if td.text.strip() else None
                )

        return formatted_data

    async def get_all_data(self, area, subarea=None):
        period_list = [i for i in range(1970, 2022)]
        urls = [
            self.requisition.create_url_link(year=year, area=area, subarea=subarea)
            for year in period_list
        ]
        response = {}

        for year, url in zip(period_list, urls):

            data = await self.get_data(url=url)

            if data is None:
                print(f"Dados não encontrados para o ano {year}. URL: {url}")
                continue

            data = self.format_data(data)

            response[f"{year}"] = data

        return response

    async def get_data_from_all_areas(self, area, SubModel):
        data = {}

        for subarea in SubModel:
            response = await self.get_all_data(area=area, subarea=subarea.name)
            data[f"{subarea.value}"] = response
        return data
