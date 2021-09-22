# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_administrator import ChatAdministrator
from ..base_object import BaseObject


class ChatAdministrators(BaseObject):
    """
    Represents a list of chat administrators
    
    :param administrators: A list of chat administrators
    :type administrators: :class:`list[ChatAdministrator]`
    
    """

    ID: str = Field("chatAdministrators", alias="@type")
    administrators: list[ChatAdministrator]

    @staticmethod
    def read(q: dict) -> ChatAdministrators:
        return ChatAdministrators.construct(**q)
