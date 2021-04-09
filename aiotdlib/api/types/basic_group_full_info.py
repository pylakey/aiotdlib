# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_invite_link import ChatInviteLink
from .chat_member import ChatMember
from .chat_photo import ChatPhoto
from ..base_object import BaseObject


class BasicGroupFullInfo(BaseObject):
    """
    Contains full information about a basic group
    
    Params:
        photo (:class:`ChatPhoto`)
            Chat photo; may be null
        
        param_description (:class:`str`)
            Group description. Updated only after the basic group is opened
        
        creator_user_id (:class:`int`)
            User identifier of the creator of the group; 0 if unknown
        
        members (:obj:`list[ChatMember]`)
            Group members
        
        invite_link (:class:`ChatInviteLink`)
            Primary invite link for this group; may be null. For chat administrators with can_invite_users right only. Updated only after the basic group is opened
        
    """

    ID: str = Field("basicGroupFullInfo", alias="@type")
    photo: typing.Optional[ChatPhoto] = None
    param_description: str
    creator_user_id: int
    members: list[ChatMember]
    invite_link: typing.Optional[ChatInviteLink] = None

    @staticmethod
    def read(q: dict) -> BasicGroupFullInfo:
        return BasicGroupFullInfo.construct(**q)
