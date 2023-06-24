# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    InputMessageContent,
)


class CreateInvoiceLink(BaseObject):
    """
    Creates a link for the given invoice; for bots only

    :param invoice: Information about the invoice of the type inputMessageInvoice
    :type invoice: :class:`InputMessageContent`
    """

    ID: typing.Literal["createInvoiceLink"] = "createInvoiceLink"
    invoice: InputMessageContent
