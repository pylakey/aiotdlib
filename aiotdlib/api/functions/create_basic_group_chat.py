# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CreateBasicGroupChat(BaseObject):
    """
    Returns an existing chat corresponding to a known basic group
    
    Params:
        basic_group_id (:class:`int`)
            Basic group identifier
        
        force (:class:`bool`)
            If true, the chat will be created without network request. In this case all information about the chat except its type, title and photo can be incorrect
        
    """

    ID: str = Field("createBasicGroupChat", alias="@type")
    basic_group_id: int
    force: bool

    @staticmethod
    def read(q: dict) -> CreateBasicGroupChat:
        return CreateBasicGroupChat.construct(**q)
