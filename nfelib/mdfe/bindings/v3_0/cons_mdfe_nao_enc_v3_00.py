"""This file was generated by xsdata, v23.6, on 2023-06-27 01:20:41

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.mdfe.bindings.v3_0.cons_mdfe_nao_enc_tipos_basico_v3_00 import TconsMdfeNaoEnc

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class ConsMdfeNaoEnc(TconsMdfeNaoEnc):
    """
    Schema de validação XML dp Pedido de Consulta MDF-e não encerrados.
    """
    class Meta:
        name = "consMDFeNaoEnc"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
