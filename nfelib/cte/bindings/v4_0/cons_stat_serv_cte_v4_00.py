"""This file was generated by xsdata, v24.4, on 2024-04-08 21:52:20

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass

from nfelib.cte.bindings.v4_0.cons_stat_serv_tipos_basico_v4_00 import (
    TconsStatServ,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class ConsStatServCte(TconsStatServ):
    """
    Schema XML de validação do Pedido de Consulta do Status do Serviço CT-e.
    """

    class Meta:
        name = "consStatServCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
