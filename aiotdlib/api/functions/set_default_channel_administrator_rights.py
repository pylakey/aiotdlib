# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatAdministratorRights


class SetDefaultChannelAdministratorRights(BaseObject):
    """
    Sets default administrator rights for adding the bot to channel chats; for bots only
    
    :param default_channel_administrator_rights: Default administrator rights for adding the bot to channels; may be null, defaults to None
    :type default_channel_administrator_rights: :class:`ChatAdministratorRights`, optional
    
    """

    ID: str = Field("setDefaultChannelAdministratorRights", alias="@type")
    default_channel_administrator_rights: typing.Optional[ChatAdministratorRights] = None

    @staticmethod
    def read(q: dict) -> SetDefaultChannelAdministratorRights:
        return SetDefaultChannelAdministratorRights.construct(**q)
