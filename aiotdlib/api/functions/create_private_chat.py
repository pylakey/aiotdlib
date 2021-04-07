# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CreatePrivateChat(BaseObject):
    """
    Returns an existing chat corresponding to a given user
    
    Params:
        user_id (:class:`int`)
            User identifier
        
        force (:class:`bool`)
            If true, the chat will be created without network request. In this case all information about the chat except its type, title and photo can be incorrect
        
    """

    ID: str = Field("createPrivateChat", alias="@type")
    user_id: int
    force: bool

    @staticmethod
    def read(q: dict) -> CreatePrivateChat:
        return CreatePrivateChat.construct(**q)
