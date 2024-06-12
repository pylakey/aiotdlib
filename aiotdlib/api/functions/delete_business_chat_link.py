# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteBusinessChatLink(BaseObject):
    """
    Deletes a business chat link of the current account

    :param link: The link to delete
    :type link: :class:`String`
    """

    ID: typing.Literal["deleteBusinessChatLink"] = Field(
        "deleteBusinessChatLink", validation_alias="@type", alias="@type"
    )
    link: String
