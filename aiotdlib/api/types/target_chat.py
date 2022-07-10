# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .internal_link_type import InternalLinkType
from ..base_object import BaseObject


class TargetChat(BaseObject):
    """
    Describes the target chat to be opened
    
    """

    ID: str = Field("targetChat", alias="@type")


class TargetChatChosen(TargetChat):
    """
    The chat needs to be chosen by the user among chats of the specified types
    
    :param allow_user_chats: True, if private chats with ordinary users are allowed
    :type allow_user_chats: :class:`bool`
    
    :param allow_bot_chats: True, if private chats with other bots are allowed
    :type allow_bot_chats: :class:`bool`
    
    :param allow_group_chats: True, if basic group and supergroup chats are allowed
    :type allow_group_chats: :class:`bool`
    
    :param allow_channel_chats: True, if channel chats are allowed
    :type allow_channel_chats: :class:`bool`
    
    """

    ID: str = Field("targetChatChosen", alias="@type")
    allow_user_chats: bool
    allow_bot_chats: bool
    allow_group_chats: bool
    allow_channel_chats: bool

    @staticmethod
    def read(q: dict) -> TargetChatChosen:
        return TargetChatChosen.construct(**q)


class TargetChatCurrent(TargetChat):
    """
    The currently opened chat needs to be kept
    
    """

    ID: str = Field("targetChatCurrent", alias="@type")

    @staticmethod
    def read(q: dict) -> TargetChatCurrent:
        return TargetChatCurrent.construct(**q)


class TargetChatInternalLink(TargetChat):
    """
    The chat needs to be open with the provided internal link
    
    :param link: An internal link pointing to the chat
    :type link: :class:`InternalLinkType`
    
    """

    ID: str = Field("targetChatInternalLink", alias="@type")
    link: InternalLinkType

    @staticmethod
    def read(q: dict) -> TargetChatInternalLink:
        return TargetChatInternalLink.construct(**q)
