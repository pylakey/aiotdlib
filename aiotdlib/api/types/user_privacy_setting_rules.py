# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .user_privacy_setting_rule import UserPrivacySettingRule
from ..base_object import BaseObject


class UserPrivacySettingRules(BaseObject):
    """
    A list of privacy rules. Rules are matched in the specified order. The first matched rule defines the privacy setting for a given user. If no rule matches, the action is not allowed
    
    Params:
        rules (:obj:`list[UserPrivacySettingRule]`)
            A list of rules
        
    """

    ID: str = Field("userPrivacySettingRules", alias="@type")
    rules: list[UserPrivacySettingRule]

    @staticmethod
    def read(q: dict) -> UserPrivacySettingRules:
        return UserPrivacySettingRules.construct(**q)
