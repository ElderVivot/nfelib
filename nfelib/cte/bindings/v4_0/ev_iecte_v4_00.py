from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvIecteDescEvento(Enum):
    INSUCESSO_NA_ENTREGA_DO_CT_E = "Insucesso na Entrega do CT-e"


class EvIecteTpMotivo(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


@dataclass
class EvIecte:
    """
    Schema XML de validação do evento insucesso na entrega eletrônico do CT-e
    110190.

    :ivar descEvento: Descrição do Evento - “Insucesso na Entrega do
        CT-e”
    :ivar nProt: Número do Protocolo de autorização do CT-e
    :ivar dhTentativaEntrega: Data e hora da tentativa da entrega da
        NF-e Formato AAAA-MM-DDTHH:MM:DD TZD
    :ivar nTentativa: Número da tentativa de entrega que não teve
        insucesso
    :ivar tpMotivo: Motivo do insucesso 1- Recebedor não encontrado; 2-
        Recusa do recebedor; 3- Endereço inexistente; 4- Outros (exige
        informar justificativa)
    :ivar xJustMotivo: Justificativa do Motivo de insucesso, informar
        apenas para tpMotivo = 4
    :ivar latitude: Latitude do ponto de entrega
    :ivar longitude: Longitude do ponto de entrega
    :ivar hashTentativaEntrega: Hash (SHA1) no formato Base64 resultante
        da concatenação: Chave de acesso do CT-e + Base64 da imagem
        capturada da tentativa com insucesso da entrega (Exemplo: foto
        do local que não recebeu a entrega ou do local sem recebedor) O
        hashCSRT é o resultado das funções SHA-1 e base64 do token CSRT
        fornecido pelo fisco + chave de acesso do DF-e. (Implementação
        em futura NT) Observação: 28 caracteres são representados no
        schema como 20 bytes do tipo base64Binary
    :ivar dhHashTentativaEntrega: Data e hora de geração do hash
        tentativa entrega Formato AAAA-MM-DDTHH:MM:DD TZD
    :ivar infEntrega: Grupo de informações das NF-e que não tiveram
        sucesso na entrega ao Destinatário Informar o grupo apenas para
        CT-e com tipo de serviço Normal
    """
    class Meta:
        name = "evIECTe"
        namespace = "http://www.portalfiscal.inf.br/cte"

    descEvento: Optional[EvIecteDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    nProt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    dhTentativaEntrega: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    nTentativa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    tpMotivo: Optional[EvIecteTpMotivo] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    xJustMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 15,
            "max_length": 256,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    latitude: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"[0-9]\.[0-9]{6}|[1-8][0-9]\.[0-9]{6}|90\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-8][0-9]\.[0-9]{6}|-90\.[0-9]{6}",
        }
    )
    longitude: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"[0-9]\.[0-9]{6}|[1-9][0-9]\.[0-9]{6}|1[0-7][0-9]\.[0-9]{6}|180\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-9][0-9]\.[0-9]{6}|-1[0-7][0-9]\.[0-9]{6}|-180\.[0-9]{6}",
        }
    )
    hashTentativaEntrega: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "length": 20,
            "format": "base64",
        }
    )
    dhHashTentativaEntrega: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    infEntrega: List["EvIecte.InfEntrega"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2000,
        }
    )

    @dataclass
    class InfEntrega:
        """
        :ivar chNFe: Chave de acesso da NF-e com insucesso na tentativa
            de entrega
        """
        chNFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
