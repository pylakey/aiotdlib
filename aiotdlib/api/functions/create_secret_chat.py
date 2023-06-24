# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CreateSecretChat(BaseObject):
    """
    Returns an existing chat corresponding to a known secret chat

    :param secret_chat_id: Secret chat identifier
    :type secret_chat_id: :class:`Int32`
    """

    ID: typing.Literal["createSecretChat"] = "createSecretChat"
    secret_chat_id: Int32
