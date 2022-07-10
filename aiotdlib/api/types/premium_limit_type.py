# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PremiumLimitType(BaseObject):
    """
    Describes type of a limit, increased for Premium users
    
    """

    ID: str = Field("premiumLimitType", alias="@type")


class PremiumLimitTypeBioLength(PremiumLimitType):
    """
    The maximum length of the user's bio
    
    """

    ID: str = Field("premiumLimitTypeBioLength", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumLimitTypeBioLength:
        return PremiumLimitTypeBioLength.construct(**q)


class PremiumLimitTypeCaptionLength(PremiumLimitType):
    """
    The maximum length of sent media caption
    
    """

    ID: str = Field("premiumLimitTypeCaptionLength", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumLimitTypeCaptionLength:
        return PremiumLimitTypeCaptionLength.construct(**q)


class PremiumLimitTypeChatFilterChosenChatCount(PremiumLimitType):
    """
    The maximum number of pinned and always included, or always excluded chats in a chat filter
    
    """

    ID: str = Field("premiumLimitTypeChatFilterChosenChatCount", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumLimitTypeChatFilterChosenChatCount:
        return PremiumLimitTypeChatFilterChosenChatCount.construct(**q)


class PremiumLimitTypeChatFilterCount(PremiumLimitType):
    """
    The maximum number of chat filters
    
    """

    ID: str = Field("premiumLimitTypeChatFilterCount", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumLimitTypeChatFilterCount:
        return PremiumLimitTypeChatFilterCount.construct(**q)


class PremiumLimitTypeCreatedPublicChatCount(PremiumLimitType):
    """
    The maximum number of created public chats
    
    """

    ID: str = Field("premiumLimitTypeCreatedPublicChatCount", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumLimitTypeCreatedPublicChatCount:
        return PremiumLimitTypeCreatedPublicChatCount.construct(**q)


class PremiumLimitTypeFavoriteStickerCount(PremiumLimitType):
    """
    The maximum number of favorite stickers
    
    """

    ID: str = Field("premiumLimitTypeFavoriteStickerCount", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumLimitTypeFavoriteStickerCount:
        return PremiumLimitTypeFavoriteStickerCount.construct(**q)


class PremiumLimitTypePinnedArchivedChatCount(PremiumLimitType):
    """
    The maximum number of pinned chats in the archive chat list
    
    """

    ID: str = Field("premiumLimitTypePinnedArchivedChatCount", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumLimitTypePinnedArchivedChatCount:
        return PremiumLimitTypePinnedArchivedChatCount.construct(**q)


class PremiumLimitTypePinnedChatCount(PremiumLimitType):
    """
    The maximum number of pinned chats in the main chat list
    
    """

    ID: str = Field("premiumLimitTypePinnedChatCount", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumLimitTypePinnedChatCount:
        return PremiumLimitTypePinnedChatCount.construct(**q)


class PremiumLimitTypeSavedAnimationCount(PremiumLimitType):
    """
    The maximum number of saved animations
    
    """

    ID: str = Field("premiumLimitTypeSavedAnimationCount", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumLimitTypeSavedAnimationCount:
        return PremiumLimitTypeSavedAnimationCount.construct(**q)


class PremiumLimitTypeSupergroupCount(PremiumLimitType):
    """
    The maximum number of joined supergroups and channels
    
    """

    ID: str = Field("premiumLimitTypeSupergroupCount", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumLimitTypeSupergroupCount:
        return PremiumLimitTypeSupergroupCount.construct(**q)
