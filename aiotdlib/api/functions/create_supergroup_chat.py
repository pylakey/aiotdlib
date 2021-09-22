# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CreateSupergroupChat(BaseObject):
    """
    Returns an existing chat corresponding to a known supergroup or channel
    
    :param supergroup_id: Supergroup or channel identifier
    :type supergroup_id: :class:`int`
    
    :param force: If true, the chat will be created without network request. In this case all information about the chat except its type, title and photo can be incorrect
    :type force: :class:`bool`
    
    """

    ID: str = Field("createSupergroupChat", alias="@type")
    supergroup_id: int
    force: bool

    @staticmethod
    def read(q: dict) -> CreateSupergroupChat:
        return CreateSupergroupChat.construct(**q)
