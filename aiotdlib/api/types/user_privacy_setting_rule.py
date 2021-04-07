# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class UserPrivacySettingRule(BaseObject):
    """
    Represents a single rule for managing privacy settings
    
    """

    ID: str = Field("userPrivacySettingRule", alias="@type")


class UserPrivacySettingRuleAllowAll(UserPrivacySettingRule):
    """
    A rule to allow all users to do something
    
    """

    ID: str = Field("userPrivacySettingRuleAllowAll", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingRuleAllowAll:
        return UserPrivacySettingRuleAllowAll.construct(**q)


class UserPrivacySettingRuleAllowChatMembers(UserPrivacySettingRule):
    """
    A rule to allow all members of certain specified basic groups and supergroups to doing something
    
    Params:
        chat_ids (:obj:`list[int]`)
            The chat identifiers, total number of chats in all rules must not exceed 20
        
    """

    ID: str = Field("userPrivacySettingRuleAllowChatMembers", alias="@type")
    chat_ids: list[int]

    @staticmethod
    def read(q: dict) -> UserPrivacySettingRuleAllowChatMembers:
        return UserPrivacySettingRuleAllowChatMembers.construct(**q)


class UserPrivacySettingRuleAllowContacts(UserPrivacySettingRule):
    """
    A rule to allow all of a user's contacts to do something
    
    """

    ID: str = Field("userPrivacySettingRuleAllowContacts", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingRuleAllowContacts:
        return UserPrivacySettingRuleAllowContacts.construct(**q)


class UserPrivacySettingRuleAllowUsers(UserPrivacySettingRule):
    """
    A rule to allow certain specified users to do something
    
    Params:
        user_ids (:obj:`list[int]`)
            The user identifiers, total number of users in all rules must not exceed 1000
        
    """

    ID: str = Field("userPrivacySettingRuleAllowUsers", alias="@type")
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> UserPrivacySettingRuleAllowUsers:
        return UserPrivacySettingRuleAllowUsers.construct(**q)


class UserPrivacySettingRuleRestrictAll(UserPrivacySettingRule):
    """
    A rule to restrict all users from doing something
    
    """

    ID: str = Field("userPrivacySettingRuleRestrictAll", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingRuleRestrictAll:
        return UserPrivacySettingRuleRestrictAll.construct(**q)


class UserPrivacySettingRuleRestrictChatMembers(UserPrivacySettingRule):
    """
    A rule to restrict all members of specified basic groups and supergroups from doing something
    
    Params:
        chat_ids (:obj:`list[int]`)
            The chat identifiers, total number of chats in all rules must not exceed 20
        
    """

    ID: str = Field("userPrivacySettingRuleRestrictChatMembers", alias="@type")
    chat_ids: list[int]

    @staticmethod
    def read(q: dict) -> UserPrivacySettingRuleRestrictChatMembers:
        return UserPrivacySettingRuleRestrictChatMembers.construct(**q)


class UserPrivacySettingRuleRestrictContacts(UserPrivacySettingRule):
    """
    A rule to restrict all contacts of a user from doing something
    
    """

    ID: str = Field("userPrivacySettingRuleRestrictContacts", alias="@type")

    @staticmethod
    def read(q: dict) -> UserPrivacySettingRuleRestrictContacts:
        return UserPrivacySettingRuleRestrictContacts.construct(**q)


class UserPrivacySettingRuleRestrictUsers(UserPrivacySettingRule):
    """
    A rule to restrict all specified users from doing something
    
    Params:
        user_ids (:obj:`list[int]`)
            The user identifiers, total number of users in all rules must not exceed 1000
        
    """

    ID: str = Field("userPrivacySettingRuleRestrictUsers", alias="@type")
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> UserPrivacySettingRuleRestrictUsers:
        return UserPrivacySettingRuleRestrictUsers.construct(**q)
