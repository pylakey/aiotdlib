# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PremiumFeature(BaseObject):
    """
    Describes a feature available to Premium users
    
    """

    ID: str = Field("premiumFeature", alias="@type")


class PremiumFeatureAdvancedChatManagement(PremiumFeature):
    """
    Ability to change position of the main chat list, archive and mute all new chats from non-contacts, and completely disable notifications about the user's contacts joined Telegram
    
    """

    ID: str = Field("premiumFeatureAdvancedChatManagement", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureAdvancedChatManagement:
        return PremiumFeatureAdvancedChatManagement.construct(**q)


class PremiumFeatureAnimatedProfilePhoto(PremiumFeature):
    """
    Profile photo animation on message and chat screens
    
    """

    ID: str = Field("premiumFeatureAnimatedProfilePhoto", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureAnimatedProfilePhoto:
        return PremiumFeatureAnimatedProfilePhoto.construct(**q)


class PremiumFeatureAppIcons(PremiumFeature):
    """
    Allowed to set a premium appllication icons
    
    """

    ID: str = Field("premiumFeatureAppIcons", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureAppIcons:
        return PremiumFeatureAppIcons.construct(**q)


class PremiumFeatureDisabledAds(PremiumFeature):
    """
    Disabled ads
    
    """

    ID: str = Field("premiumFeatureDisabledAds", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureDisabledAds:
        return PremiumFeatureDisabledAds.construct(**q)


class PremiumFeatureImprovedDownloadSpeed(PremiumFeature):
    """
    Improved download speed
    
    """

    ID: str = Field("premiumFeatureImprovedDownloadSpeed", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureImprovedDownloadSpeed:
        return PremiumFeatureImprovedDownloadSpeed.construct(**q)


class PremiumFeatureIncreasedLimits(PremiumFeature):
    """
    Increased limits
    
    """

    ID: str = Field("premiumFeatureIncreasedLimits", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureIncreasedLimits:
        return PremiumFeatureIncreasedLimits.construct(**q)


class PremiumFeatureIncreasedUploadFileSize(PremiumFeature):
    """
    Increased maximum upload file size
    
    """

    ID: str = Field("premiumFeatureIncreasedUploadFileSize", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureIncreasedUploadFileSize:
        return PremiumFeatureIncreasedUploadFileSize.construct(**q)


class PremiumFeatureProfileBadge(PremiumFeature):
    """
    A badge in the user's profile
    
    """

    ID: str = Field("premiumFeatureProfileBadge", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureProfileBadge:
        return PremiumFeatureProfileBadge.construct(**q)


class PremiumFeatureUniqueReactions(PremiumFeature):
    """
    Allowed to use more reactions
    
    """

    ID: str = Field("premiumFeatureUniqueReactions", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureUniqueReactions:
        return PremiumFeatureUniqueReactions.construct(**q)


class PremiumFeatureUniqueStickers(PremiumFeature):
    """
    Allowed to use premium stickers with unique effects
    
    """

    ID: str = Field("premiumFeatureUniqueStickers", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureUniqueStickers:
        return PremiumFeatureUniqueStickers.construct(**q)


class PremiumFeatureVoiceRecognition(PremiumFeature):
    """
    The ability to convert voice notes to text
    
    """

    ID: str = Field("premiumFeatureVoiceRecognition", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumFeatureVoiceRecognition:
        return PremiumFeatureVoiceRecognition.construct(**q)
