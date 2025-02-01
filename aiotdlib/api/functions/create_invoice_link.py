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

    :param business_connection_id: Unique identifier of business connection on behalf of which to send the request
    :type business_connection_id: :class:`String`
    :param invoice: Information about the invoice of the type inputMessageInvoice
    :type invoice: :class:`InputMessageContent`
    """

    ID: typing.Literal["createInvoiceLink"] = Field("createInvoiceLink", validation_alias="@type", alias="@type")
    business_connection_id: String
    invoice: InputMessageContent
