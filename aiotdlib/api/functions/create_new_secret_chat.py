# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CreateNewSecretChat(BaseObject):
    """
    Creates a new secret chat. Returns the newly created chat

    :param user_id: Identifier of the target user
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["createNewSecretChat"] = Field("createNewSecretChat", validation_alias="@type", alias="@type")
    user_id: Int53
