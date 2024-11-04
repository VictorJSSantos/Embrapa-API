from enum import Enum


class ProductionModel(str, Enum):
    opt_02 = "Produção"


class ProcessingModel(str, Enum):
    opt_03 = "Processamento"


class ProcessingSubModel(str, Enum):

    subopt_01 = "Viníferas"
    subopt_02 = "Americanas e Híbridas"
    subopt_03 = "Uvas de Mesa"
    subopt_04 = "Sem Classificação"


class SalesModel(str, Enum):
    opt_04 = "Comercialização"


class ImportsModel(str, Enum):
    opt_05 = "Importação"


class ImportsSubModel(str, Enum):
    subopt_01 = "Vinhos de Mesa"
    subopt_02 = "Espumantes"
    subopt_03 = "Uvas Frescas"
    subopt_04 = "Uvas Passas"
    subopt_05 = "Suco de Uva"


class ExportsModel(str, Enum):
    opt_06 = "Exportação"


class ExportsSubModel(str, Enum):
    subopt_01 = "Vinhos de Mesa"
    subopt_02 = "Espumantes"
    subopt_03 = "Uvas Frescas"
    subopt_04 = "Suco de Uva"
