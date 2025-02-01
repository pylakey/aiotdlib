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
    MessageSender,
)


class GetStarAdAccountUrl(BaseObject):
    """
    Returns a URL for a Telegram Ad platform account that can be used to set up advertisements for the chat paid in the owned Telegram Stars

    :param owner_id: Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of an owned channel chat
    :type owner_id: :class:`MessageSender`
    """

    ID: typing.Literal["getStarAdAccountUrl"] = Field("getStarAdAccountUrl", validation_alias="@type", alias="@type")
    owner_id: MessageSender
