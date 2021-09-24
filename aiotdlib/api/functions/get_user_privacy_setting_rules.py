# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import UserPrivacySetting


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
