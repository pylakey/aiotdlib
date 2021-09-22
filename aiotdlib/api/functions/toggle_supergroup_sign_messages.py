# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ToggleSupergroupSignMessages(BaseObject):
    """
    Toggles sender signatures messages sent in a channel; requires can_change_info administrator right
    
    :param supergroup_id: Identifier of the channel
    :type supergroup_id: :class:`int`
    
    :param sign_messages: New value of sign_messages
    :type sign_messages: :class:`bool`
    
    """

    ID: str = Field("toggleSupergroupSignMessages", alias="@type")
    supergroup_id: int
    sign_messages: bool

    @staticmethod
    def read(q: dict) -> ToggleSupergroupSignMessages:
        return ToggleSupergroupSignMessages.construct(**q)
