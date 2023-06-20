# Copyright 2018 - TODAY Luis Felipe Mileo - KMEE INFORMATICA LTDA
# Copyright 2023 - TODAY Akretion - Raphaël Valyi <raphael.valyi@akretion.com>

from erpbrasil.assinatura.assinatura import Assinatura
from dataclasses import is_dataclass

try:
    from erpbrasil.edoc.edoc import DocumentoEletronico
    from erpbrasil.edoc.resposta import RetornoSoap, analisar_retorno_raw
    from erpbrasil.edoc.nfe import NFe

except ImportError:
    raise RuntimeError(
        "You need to install the erpbrasil.edoc package to use this legacy webservice layer."
    )

from lxml import etree
from lxml.etree import _Element
import re
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


def analisar_retorno_raw_xsdata(operacao, raiz, xml, retorno, classe):
    retorno.raise_for_status()
    match = re.search("<soap:Body>(.*?)</soap:Body>", retorno.text.replace("\n", ""))
    if match:
        xml_resposta = match.group(1)
        # pega a resposta de dentro do envelope
        resultado = etree.tostring(etree.fromstring(xml_resposta)[0])
        parser = XmlParser(context=XmlContext())
        resposta = parser.from_string(resultado.decode(), classe)
        return RetornoSoap(operacao, raiz, xml, retorno, resposta)


class DocumentoElectronicoAdapter(DocumentoEletronico):
    def render_edoc_xsdata(self, edoc, pretty_print=False):
        """
        Same as render_edoc but compatible with xsdata bindings.
        """
        if isinstance(edoc, _Element):
            return etree.tostring(edoc), edoc
        if isinstance(edoc, str):
            return edoc, etree.fromstring(edoc)
        serializer = XmlSerializer(config=SerializerConfig(pretty_print=pretty_print))

        if self._namespace:
            ns_map = {None: self._namespace}
        else:
            ns_map = None

        xml_string = serializer.render(obj=edoc, ns_map=ns_map)
        return xml_string, etree.fromstring(xml_string.encode())

    def _post(self, raiz, url, operacao, classe):
        """
        Same as _post but compatible with xsdata bindings.
        """
        if is_dataclass(raiz):
            xml_string, xml_etree = self.render_edoc_xsdata(raiz)
        else:
            xml_string, xml_etree = self._generateds_to_string_etree(raiz)
        with self._transmissao.cliente(url):
            retorno = self._transmissao.enviar(operacao, xml_etree)
            if is_dataclass(raiz):
                return analisar_retorno_raw_xsdata(
                    operacao, raiz, xml_string, retorno, classe
                )
            else:
                return analisar_retorno_raw(operacao, raiz, xml_string, retorno, classe)

    def assina_raiz(self, raiz, id, getchildren=False):
        """
        Same as assina_raiz but compatible with xsdata bindings.
        """
        if is_dataclass(raiz):
            xml_etree = self.render_edoc_xsdata(raiz)[1]
            xml_assinado = Assinatura(self._transmissao.certificado).assina_xml2(
                xml_etree, id, getchildren
            )
        else:
            xml_string, xml_etree = self._generateds_to_string_etree(raiz)
            xml_assinado = Assinatura(self._transmissao.certificado).assina_xml2(
                xml_etree, id, getchildren
            )
        return xml_assinado


class NFeAdapter(DocumentoElectronicoAdapter, NFe):
    pass