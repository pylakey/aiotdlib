# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class UserPrivacySetting(BaseObject):
    """
    Describes available user privacy settings
    
    """

    ID: str = Field("userPrivacySetting", alias="@type")


class UserPrivacySettingAllowCalls(UserPrivacySetting):
    """
    A privacy setting for managing whether the user can be called
    
    """

    ID: str = Field("userPrivacySettingAllowCalls", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingAllowCalls:
        return UserPrivacySettingAllowCalls.construct(**q)


class UserPrivacySettingAllowChatInvites(UserPrivacySetting):
    """
    A privacy setting for managing whether the user can be invited to chats
    
    """

    ID: str = Field("userPrivacySettingAllowChatInvites", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingAllowChatInvites:
        return UserPrivacySettingAllowChatInvites.construct(**q)


class UserPrivacySettingAllowFindingByPhoneNumber(UserPrivacySetting):
    """
    A privacy setting for managing whether the user can be found by their phone number. Checked only if the phone number is not known to the other user. Can be set only to "Allow contacts" or "Allow all"
    
    """

    ID: str = Field("userPrivacySettingAllowFindingByPhoneNumber", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingAllowFindingByPhoneNumber:
        return UserPrivacySettingAllowFindingByPhoneNumber.construct(**q)


class UserPrivacySettingAllowPeerToPeerCalls(UserPrivacySetting):
    """
    A privacy setting for managing whether peer-to-peer connections can be used for calls
    
    """

    ID: str = Field("userPrivacySettingAllowPeerToPeerCalls", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingAllowPeerToPeerCalls:
        return UserPrivacySettingAllowPeerToPeerCalls.construct(**q)


class UserPrivacySettingShowLinkInForwardedMessages(UserPrivacySetting):
    """
    A privacy setting for managing whether a link to the user's account is included in forwarded messages
    
    """

    ID: str = Field("userPrivacySettingShowLinkInForwardedMessages", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingShowLinkInForwardedMessages:
        return UserPrivacySettingShowLinkInForwardedMessages.construct(**q)


class UserPrivacySettingShowPhoneNumber(UserPrivacySetting):
    """
    A privacy setting for managing whether the user's phone number is visible
    
    """

    ID: str = Field("userPrivacySettingShowPhoneNumber", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingShowPhoneNumber:
        return UserPrivacySettingShowPhoneNumber.construct(**q)


class UserPrivacySettingShowProfilePhoto(UserPrivacySetting):
    """
    A privacy setting for managing whether the user's profile photo is visible
    
    """

    ID: str = Field("userPrivacySettingShowProfilePhoto", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingShowProfilePhoto:
        return UserPrivacySettingShowProfilePhoto.construct(**q)


class UserPrivacySettingShowStatus(UserPrivacySetting):
    """
    A privacy setting for managing whether the user's online status is visible
    
    """

    ID: str = Field("userPrivacySettingShowStatus", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingShowStatus:
        return UserPrivacySettingShowStatus.construct(**q)
