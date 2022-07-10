# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleSupergroupJoinToSendMessages(BaseObject):
    """
    Toggles whether joining is mandatory to send messages to a discussion supergroup; requires can_restrict_members administrator right
    
    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`int`
    
    :param join_to_send_messages: New value of join_to_send_messages
    :type join_to_send_messages: :class:`bool`
    
    """

    ID: str = Field("toggleSupergroupJoinToSendMessages", alias="@type")
    supergroup_id: int
    join_to_send_messages: bool

    @staticmethod
    def read(q: dict) -> ToggleSupergroupJoinToSendMessages:
        return ToggleSupergroupJoinToSendMessages.construct(**q)
