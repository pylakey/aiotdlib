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
    ChatAdministratorRights,
)


class SetDefaultGroupAdministratorRights(BaseObject):
    """
    Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only

    :param default_group_administrator_rights: Default administrator rights for adding the bot to basic group and supergroup chats; pass null to remove default rights, defaults to None
    :type default_group_administrator_rights: :class:`ChatAdministratorRights`, optional
    """

    ID: typing.Literal["setDefaultGroupAdministratorRights"] = "setDefaultGroupAdministratorRights"
    default_group_administrator_rights: typing.Optional[ChatAdministratorRights] = None
