# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleSessionCanAcceptSecretChats(BaseObject):
    """
    Toggles whether a session can accept incoming secret chats
    
    :param session_id: Session identifier
    :type session_id: :class:`int`
    
    :param can_accept_secret_chats: True, if incoming secret chats can be accepted by the session
    :type can_accept_secret_chats: :class:`bool`
    
    """

    ID: str = Field("toggleSessionCanAcceptSecretChats", alias="@type")
    session_id: int
    can_accept_secret_chats: bool

    @staticmethod
    def read(q: dict) -> ToggleSessionCanAcceptSecretChats:
        return ToggleSessionCanAcceptSecretChats.construct(**q)
