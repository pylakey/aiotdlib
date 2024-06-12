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
    InputBusinessChatLink,
)


class EditBusinessChatLink(BaseObject):
    """
    Edits a business chat link of the current account. Requires Telegram Business subscription. Returns the edited link

    :param link: The link to edit
    :type link: :class:`String`
    :param link_info: New description of the link
    :type link_info: :class:`InputBusinessChatLink`
    """

    ID: typing.Literal["editBusinessChatLink"] = Field("editBusinessChatLink", validation_alias="@type", alias="@type")
    link: String
    link_info: InputBusinessChatLink
