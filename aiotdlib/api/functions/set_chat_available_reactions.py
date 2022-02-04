# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetChatAvailableReactions(BaseObject):
    """
    Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param available_reactions: New list of reactions, available in the chat. All reactions must be active and order of the reactions must be the same as in updateReactions
    :type available_reactions: :class:`list[str]`
    
    """

    ID: str = Field("setChatAvailableReactions", alias="@type")
    chat_id: int
    available_reactions: list[str]

    @staticmethod
    def read(q: dict) -> SetChatAvailableReactions:
        return SetChatAvailableReactions.construct(**q)
