# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleSupergroupSignMessages(BaseObject):
    """
    Toggles sender signatures messages sent in a channel; requires can_change_info administrator right
    
    Params:
        supergroup_id (:class:`int`)
            Identifier of the channel
        
        sign_messages (:class:`bool`)
            New value of sign_messages
        
    """

    ID: str = Field("toggleSupergroupSignMessages", alias="@type")
    supergroup_id: int
    sign_messages: bool

    @staticmethod
    def read(q: dict) -> ToggleSupergroupSignMessages:
        return ToggleSupergroupSignMessages.construct(**q)
