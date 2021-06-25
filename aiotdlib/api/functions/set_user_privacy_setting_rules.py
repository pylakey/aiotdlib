# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import UserPrivacySetting
from ..types import UserPrivacySettingRules


class SetUserPrivacySettingRules(BaseObject):
    """
    Changes user privacy settings
    
    Params:
        setting (:class:`UserPrivacySetting`)
            The privacy setting
        
        rules (:class:`UserPrivacySettingRules`)
            The new privacy rules
        
    """

    ID: str = Field("setUserPrivacySettingRules", alias="@type")
    setting: UserPrivacySetting
    rules: UserPrivacySettingRules

    @staticmethod
    def read(q: dict) -> SetUserPrivacySettingRules:
        return SetUserPrivacySettingRules.construct(**q)
