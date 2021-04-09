# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_photo_info import ChatPhotoInfo
from .chat_type import ChatType
from ..base_object import BaseObject


class ChatInviteLinkInfo(BaseObject):
    """
    Contains information about a chat invite link
    
    Params:
        chat_id (:class:`int`)
            Chat identifier of the invite link; 0 if the user has no access to the chat before joining
        
        accessible_for (:class:`int`)
            If non-zero, the amount of time for which read access to the chat will remain available, in seconds
        
        type_ (:class:`ChatType`)
            Contains information about the type of the chat
        
        title (:class:`str`)
            Title of the chat
        
        photo (:class:`ChatPhotoInfo`)
            Chat photo; may be null
        
        member_count (:class:`int`)
            Number of members in the chat
        
        member_user_ids (:obj:`list[int]`)
            User identifiers of some chat members that may be known to the current user
        
        is_public (:class:`bool`)
            True, if the chat is a public supergroup or channel, i.e. it has a username or it is a location-based supergroup
        
    """

    ID: str = Field("chatInviteLinkInfo", alias="@type")
    chat_id: int
    accessible_for: int
    type_: ChatType = Field(..., alias='type')
    title: str
    photo: typing.Optional[ChatPhotoInfo] = None
    member_count: int
    member_user_ids: list[int]
    is_public: bool

    @staticmethod
    def read(q: dict) -> ChatInviteLinkInfo:
        return ChatInviteLinkInfo.construct(**q)
