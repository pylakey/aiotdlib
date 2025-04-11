# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSecretChat(BaseObject):
    """
    Returns information about a secret chat by its identifier. This is an offline method

    :param secret_chat_id: Secret chat identifier
    :type secret_chat_id: :class:`Int32`
    """

    ID: typing.Literal["getSecretChat"] = Field("getSecretChat", validation_alias="@type", alias="@type")
    secret_chat_id: Int32
