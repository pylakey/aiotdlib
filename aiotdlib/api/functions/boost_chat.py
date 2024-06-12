# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class BoostChat(BaseObject):
    """
    Boosts a chat and returns the list of available chat boost slots for the current user after the boost

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param slot_ids: Identifiers of boost slots of the current user from which to apply boosts to the chat
    :type slot_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["boostChat"] = Field("boostChat", validation_alias="@type", alias="@type")
    chat_id: Int53
    slot_ids: Vector[Int32]
