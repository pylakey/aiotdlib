# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ProcessChatJoinRequests(BaseObject):
    """
    Handles all pending join requests for a given link in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param invite_link: Invite link for which to process join requests. If empty, all join requests will be processed. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    :type invite_link: :class:`str`
    
    :param approve: Pass true to approve all requests; pass false to decline them
    :type approve: :class:`bool`
    
    """

    ID: str = Field("processChatJoinRequests", alias="@type")
    chat_id: int
    invite_link: str
    approve: bool

    @staticmethod
    def read(q: dict) -> ProcessChatJoinRequests:
        return ProcessChatJoinRequests.construct(**q)
