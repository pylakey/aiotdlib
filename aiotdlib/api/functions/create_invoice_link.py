# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputMessageContent


class CreateInvoiceLink(BaseObject):
    """
    Creates a link for the given invoice; for bots only
    
    :param invoice: Information about the invoice of the type inputMessageInvoice
    :type invoice: :class:`InputMessageContent`
    
    """

    ID: str = Field("createInvoiceLink", alias="@type")
    invoice: InputMessageContent

    @staticmethod
    def read(q: dict) -> CreateInvoiceLink:
        return CreateInvoiceLink.construct(**q)
