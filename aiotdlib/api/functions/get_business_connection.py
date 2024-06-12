# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBusinessConnection(BaseObject):
    """
    Returns information about a business connection by its identifier; for bots only

    :param connection_id: Identifier of the business connection to return
    :type connection_id: :class:`String`
    """

    ID: typing.Literal["getBusinessConnection"] = Field(
        "getBusinessConnection", validation_alias="@type", alias="@type"
    )
    connection_id: String
