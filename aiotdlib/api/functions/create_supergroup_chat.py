# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CreateSupergroupChat(BaseObject):
    """
    Returns an existing chat corresponding to a known supergroup or channel
    
    Params:
        supergroup_id (:class:`int`)
            Supergroup or channel identifier
        
        force (:class:`bool`)
            If true, the chat will be created without network request. In this case all information about the chat except its type, title and photo can be incorrect
        
    """

    ID: str = Field("createSupergroupChat", alias="@type")
    supergroup_id: int
    force: bool

    @staticmethod
    def read(q: dict) -> CreateSupergroupChat:
        return CreateSupergroupChat.construct(**q)
