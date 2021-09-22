# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CreateBasicGroupChat(BaseObject):
    """
    Returns an existing chat corresponding to a known basic group
    
    :param basic_group_id: Basic group identifier
    :type basic_group_id: :class:`int`
    
    :param force: If true, the chat will be created without network request. In this case all information about the chat except its type, title and photo can be incorrect
    :type force: :class:`bool`
    
    """

    ID: str = Field("createBasicGroupChat", alias="@type")
    basic_group_id: int
    force: bool

    @staticmethod
    def read(q: dict) -> CreateBasicGroupChat:
        return CreateBasicGroupChat.construct(**q)
