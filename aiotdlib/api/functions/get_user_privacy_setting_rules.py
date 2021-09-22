# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import UserPrivacySetting
from ..base_object import BaseObject


class GetUserPrivacySettingRules(BaseObject):
    """
    Returns the current privacy settings
    
    :param setting: The privacy setting
    :type setting: :class:`UserPrivacySetting`
    
    """

    ID: str = Field("getUserPrivacySettingRules", alias="@type")
    setting: UserPrivacySetting

    @staticmethod
    def read(q: dict) -> GetUserPrivacySettingRules:
        return GetUserPrivacySettingRules.construct(**q)
