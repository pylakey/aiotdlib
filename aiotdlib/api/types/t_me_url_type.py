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
    
    :param info: Information about the chat invite link
    :type info: :class:`ChatInviteLinkInfo`
    
    """

    ID: str = Field("tMeUrlTypeChatInvite", alias="@type")
    info: ChatInviteLinkInfo

    @staticmethod
    def read(q: dict) -> TMeUrlTypeChatInvite:
        return TMeUrlTypeChatInvite.construct(**q)


class TMeUrlTypeStickerSet(TMeUrlType):
    """
    A URL linking to a sticker set
    
    :param sticker_set_id: Identifier of the sticker set
    :type sticker_set_id: :class:`int`
    
    """

    ID: str = Field("tMeUrlTypeStickerSet", alias="@type")
    sticker_set_id: int

    @staticmethod
    def read(q: dict) -> TMeUrlTypeStickerSet:
        return TMeUrlTypeStickerSet.construct(**q)


class TMeUrlTypeSupergroup(TMeUrlType):
    """
    A URL linking to a public supergroup or channel
    
    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`int`
    
    """

    ID: str = Field("tMeUrlTypeSupergroup", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> TMeUrlTypeSupergroup:
        return TMeUrlTypeSupergroup.construct(**q)


class TMeUrlTypeUser(TMeUrlType):
    """
    A URL linking to a user
    
    :param user_id: Identifier of the user
    :type user_id: :class:`int`
    
    """

    ID: str = Field("tMeUrlTypeUser", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> TMeUrlTypeUser:
        return TMeUrlTypeUser.construct(**q)
