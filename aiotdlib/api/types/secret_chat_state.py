# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SecretChatState(BaseObject):
    """
    Describes the current secret chat state
    
    """

    ID: str = Field("secretChatState", alias="@type")


class SecretChatStateClosed(SecretChatState):
    """
    The secret chat is closed
    
    """

    ID: str = Field("secretChatStateClosed", alias="@type")

    @staticmethod
    def read(q: dict) -> SecretChatStateClosed:
        return SecretChatStateClosed.construct(**q)


class SecretChatStatePending(SecretChatState):
    """
    The secret chat is not yet created; waiting for the other user to get online
    
    """

    ID: str = Field("secretChatStatePending", alias="@type")

    @staticmethod
    def read(q: dict) -> SecretChatStatePending:
        return SecretChatStatePending.construct(**q)


class SecretChatStateReady(SecretChatState):
    """
    The secret chat is ready to use
    
    """

    ID: str = Field("secretChatStateReady", alias="@type")

    @staticmethod
    def read(q: dict) -> SecretChatStateReady:
        return SecretChatStateReady.construct(**q)
