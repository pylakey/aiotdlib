# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_invite_link_info import ChatInviteLinkInfo
from ..base_object import BaseObject


class TMeUrlType(BaseObject):
    """
    Describes the type of a URL linking to an internal Telegram entity
    
    """

    ID: str = Field("tMeUrlType", alias="@type")


class TMeUrlTypeChatInvite(TMeUrlType):
    """
    A chat invite link
    
    Params:
        info (:class:`ChatInviteLinkInfo`)
            Chat invite link info
        
    """

    ID: str = Field("tMeUrlTypeChatInvite", alias="@type")
    info: ChatInviteLinkInfo

    @staticmethod
    def read(q: dict) -> TMeUrlTypeChatInvite:
        return TMeUrlTypeChatInvite.construct(**q)


class TMeUrlTypeStickerSet(TMeUrlType):
    """
    A URL linking to a sticker set
    
    Params:
        sticker_set_id (:class:`int`)
            Identifier of the sticker set
        
    """

    ID: str = Field("tMeUrlTypeStickerSet", alias="@type")
    sticker_set_id: int

    @staticmethod
    def read(q: dict) -> TMeUrlTypeStickerSet:
        return TMeUrlTypeStickerSet.construct(**q)


class TMeUrlTypeSupergroup(TMeUrlType):
    """
    A URL linking to a public supergroup or channel
    
    Params:
        supergroup_id (:class:`int`)
            Identifier of the supergroup or channel
        
    """

    ID: str = Field("tMeUrlTypeSupergroup", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> TMeUrlTypeSupergroup:
        return TMeUrlTypeSupergroup.construct(**q)


class TMeUrlTypeUser(TMeUrlType):
    """
    A URL linking to a user
    
    Params:
        user_id (:class:`int`)
            Identifier of the user
        
    """

    ID: str = Field("tMeUrlTypeUser", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> TMeUrlTypeUser:
        return TMeUrlTypeUser.construct(**q)
