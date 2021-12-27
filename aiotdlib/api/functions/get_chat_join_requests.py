# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatJoinRequest


class GetChatJoinRequests(BaseObject):
    """
    Returns pending join requests in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param invite_link: Invite link for which to return join requests. If empty, all join requests will be returned. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    :type invite_link: :class:`str`
    
    :param query: A query to search for in the first names, last names and usernames of the users to return
    :type query: :class:`str`
    
    :param offset_request: A chat join request from which to return next requests; pass null to get results from the beginning
    :type offset_request: :class:`ChatJoinRequest`
    
    :param limit: The maximum number of requests to join the chat to return
    :type limit: :class:`int`
    
    """

    ID: str = Field("getChatJoinRequests", alias="@type")
    chat_id: int
    invite_link: str
    query: str
    offset_request: ChatJoinRequest
    limit: int

    @staticmethod
    def read(q: dict) -> GetChatJoinRequests:
        return GetChatJoinRequests.construct(**q)
