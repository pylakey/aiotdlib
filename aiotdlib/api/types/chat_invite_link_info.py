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
    
    :param chat_id: Chat identifier of the invite link; 0 if the user has no access to the chat before joining
    :type chat_id: :class:`int`
    
    :param accessible_for: If non-zero, the amount of time for which read access to the chat will remain available, in seconds
    :type accessible_for: :class:`int`
    
    :param type_: Type of the chat
    :type type_: :class:`ChatType`
    
    :param title: Title of the chat
    :type title: :class:`str`
    
    :param photo: Chat photo; may be null, defaults to None
    :type photo: :class:`ChatPhotoInfo`, optional
    
    :param param_description: Chat description
    :type param_description: :class:`str`
    
    :param member_count: Number of members in the chat
    :type member_count: :class:`int`
    
    :param member_user_ids: User identifiers of some chat members that may be known to the current user
    :type member_user_ids: :class:`list[int]`
    
    :param creates_join_request: True, if the link only creates join request
    :type creates_join_request: :class:`bool`
    
    :param is_public: True, if the chat is a public supergroup or channel, i.e. it has a username or it is a location-based supergroup
    :type is_public: :class:`bool`
    
    """

    ID: str = Field("chatInviteLinkInfo", alias="@type")
    chat_id: int
    accessible_for: int
    type_: ChatType = Field(..., alias='type')
    title: str
    photo: typing.Optional[ChatPhotoInfo] = None
    param_description: str
    member_count: int
    member_user_ids: list[int]
    creates_join_request: bool
    is_public: bool

    @staticmethod
    def read(q: dict) -> ChatInviteLinkInfo:
        return ChatInviteLinkInfo.construct(**q)
