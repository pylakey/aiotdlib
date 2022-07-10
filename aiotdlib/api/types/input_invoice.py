# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class InputInvoice(BaseObject):
    """
    Describe an invoice to process
    
    """

    ID: str = Field("inputInvoice", alias="@type")


class InputInvoiceMessage(InputInvoice):
    """
    An invoice from a message of the type messageInvoice
    
    :param chat_id: Chat identifier of the message
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    """

    ID: str = Field("inputInvoiceMessage", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> InputInvoiceMessage:
        return InputInvoiceMessage.construct(**q)


class InputInvoiceName(InputInvoice):
    """
    An invoice from a link of the type internalLinkTypeInvoice
    
    :param name: Name of the invoice
    :type name: :class:`str`
    
    """

    ID: str = Field("inputInvoiceName", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> InputInvoiceName:
        return InputInvoiceName.construct(**q)
