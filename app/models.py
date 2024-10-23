from enum import Enum


# from pydantic import BaseModel


class ProducaoModelo(str, Enum):
    opt_02 = "Produção"


class ProcessamentoModelo(str, Enum):
    opt_03 = "Processamento"


class ProcessamentoSubModelo(str, Enum):

    subopt_01 = "Viníferas"
    subopt_02 = "Americanas e Híbridas"
    subopt_03 = "Uvas de Mesa"
    subpot_04 = "Sem Classificação"


objB = ProcessamentoSubModelo["subopt_02"]
print(objB.name)


class ComercializacaoModelo(str, Enum):
    opt_04 = "Comercialização"


class ImportacaoModelo(str, Enum):
    opt_05 = "Importação"


class ImportacaoSubModelo(str, Enum):
    subopt_01 = "Vinhos de Mesa"
    subopt_02 = "Espumantes"
    subopt_03 = "Uvas Frescas"
    subopt_04 = "Uvas Passas"
    subopt_05 = "Suco de Uva"


class ExportacaoModelo(str, Enum):
    opt_06 = "Exportação"


class ExportacaoSubModelo(str, Enum):
    subopt_01 = "Vinhos de Mesa"
    subopt_02 = "Espumantes"
    subopt_03 = "Uvas Frescas"
    subopt_04 = "Suco de Uva"


# # Classe para autenticação Bearer
# class BearerToken(HTTPBearer):
#     def __init__(self):
#         super().__init__()
