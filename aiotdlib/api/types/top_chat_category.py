# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TopChatCategory(BaseObject):
    """
    Represents the categories of chats for which a list of frequently used chats can be retrieved
    
    """

    ID: str = Field("topChatCategory", alias="@type")


class TopChatCategoryBots(TopChatCategory):
    """
    A category containing frequently used private chats with bot users
    
    """

    ID: str = Field("topChatCategoryBots", alias="@type")

    @staticmethod
    def read(q: dict) -> TopChatCategoryBots:
        return TopChatCategoryBots.construct(**q)


class TopChatCategoryCalls(TopChatCategory):
    """
    A category containing frequently used chats used for calls
    
    """

    ID: str = Field("topChatCategoryCalls", alias="@type")

    @staticmethod
    def read(q: dict) -> TopChatCategoryCalls:
        return TopChatCategoryCalls.construct(**q)


class TopChatCategoryChannels(TopChatCategory):
    """
    A category containing frequently used channels
    
    """

    ID: str = Field("topChatCategoryChannels", alias="@type")

    @staticmethod
    def read(q: dict) -> TopChatCategoryChannels:
        return TopChatCategoryChannels.construct(**q)


class TopChatCategoryForwardChats(TopChatCategory):
    """
    A category containing frequently used chats used to forward messages
    
    """

    ID: str = Field("topChatCategoryForwardChats", alias="@type")

    @staticmethod
    def read(q: dict) -> TopChatCategoryForwardChats:
        return TopChatCategoryForwardChats.construct(**q)


class TopChatCategoryGroups(TopChatCategory):
    """
    A category containing frequently used basic groups and supergroups
    
    """

    ID: str = Field("topChatCategoryGroups", alias="@type")

    @staticmethod
    def read(q: dict) -> TopChatCategoryGroups:
        return TopChatCategoryGroups.construct(**q)


class TopChatCategoryInlineBots(TopChatCategory):
    """
    A category containing frequently used chats with inline bots sorted by their usage in inline mode
    
    """

    ID: str = Field("topChatCategoryInlineBots", alias="@type")

    @staticmethod
    def read(q: dict) -> TopChatCategoryInlineBots:
        return TopChatCategoryInlineBots.construct(**q)


class TopChatCategoryUsers(TopChatCategory):
    """
    A category containing frequently used private chats with non-bot users
    
    """

    ID: str = Field("topChatCategoryUsers", alias="@type")

    @staticmethod
    def read(q: dict) -> TopChatCategoryUsers:
        return TopChatCategoryUsers.construct(**q)
