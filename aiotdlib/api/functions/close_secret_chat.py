# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CloseSecretChat(BaseObject):
    """
    Closes a secret chat, effectively transferring its state to secretChatStateClosed

    :param secret_chat_id: Secret chat identifier
    :type secret_chat_id: :class:`Int32`
    """

    ID: typing.Literal["closeSecretChat"] = "closeSecretChat"
    secret_chat_id: Int32
