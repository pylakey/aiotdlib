# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import UserPrivacySetting
from ..types import UserPrivacySettingRules
from ..base_object import BaseObject


class SetUserPrivacySettingRules(BaseObject):
    """
    Changes user privacy settings
    
    :param setting: The privacy setting
    :type setting: :class:`UserPrivacySetting`
    
    :param rules: The new privacy rules
    :type rules: :class:`UserPrivacySettingRules`
    
    """

    ID: str = Field("setUserPrivacySettingRules", alias="@type")
    setting: UserPrivacySetting
    rules: UserPrivacySettingRules

    @staticmethod
    def read(q: dict) -> SetUserPrivacySettingRules:
        return SetUserPrivacySettingRules.construct(**q)
