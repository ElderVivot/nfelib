"""This file was generated by xsdata, v24.4, on 2024-04-08 21:52:20

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass

from nfelib.cte.bindings.v4_0.evento_cte_tipos_basico_v4_00 import TretEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetEventoCte(TretEvento):
    """
    Schema XML de validação do retorno Pedido de Evento do CT-e.
    """

    class Meta:
        name = "retEventoCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
