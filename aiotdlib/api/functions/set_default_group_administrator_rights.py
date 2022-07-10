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


class SetDefaultGroupAdministratorRights(BaseObject):
    """
    Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only
    
    :param default_group_administrator_rights: Default administrator rights for adding the bot to basic group and supergroup chats; may be null, defaults to None
    :type default_group_administrator_rights: :class:`ChatAdministratorRights`, optional
    
    """

    ID: str = Field("setDefaultGroupAdministratorRights", alias="@type")
    default_group_administrator_rights: typing.Optional[ChatAdministratorRights] = None

    @staticmethod
    def read(q: dict) -> SetDefaultGroupAdministratorRights:
        return SetDefaultGroupAdministratorRights.construct(**q)
