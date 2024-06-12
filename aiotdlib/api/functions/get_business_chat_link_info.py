# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBusinessChatLinkInfo(BaseObject):
    """
    Returns information about a business chat link

    :param link_name: Name of the link
    :type link_name: :class:`String`
    """

    ID: typing.Literal["getBusinessChatLinkInfo"] = Field(
        "getBusinessChatLinkInfo", validation_alias="@type", alias="@type"
    )
    link_name: String
