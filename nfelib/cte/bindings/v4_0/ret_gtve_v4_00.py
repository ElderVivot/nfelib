"""This file was generated by xsdata, v24.4, on 2024-04-08 21:52:20

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass

from nfelib.cte.bindings.v4_0.cte_tipos_basico_v4_00 import TretGtve

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetGtve(TretGtve):
    """
    Schema XML de validação do retorno do recibo de envio da GTV-e (Modelo 64)
    """

    class Meta:
        name = "retGTVe"
        namespace = "http://www.portalfiscal.inf.br/cte"
