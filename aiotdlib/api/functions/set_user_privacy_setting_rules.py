# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    UserPrivacySetting,
    UserPrivacySettingRules,
)


class SetUserPrivacySettingRules(BaseObject):
    """
    Changes user privacy settings

    :param setting: The privacy setting
    :type setting: :class:`UserPrivacySetting`
    :param rules: The new privacy rules
    :type rules: :class:`UserPrivacySettingRules`
    """

    ID: typing.Literal["setUserPrivacySettingRules"] = "setUserPrivacySettingRules"
    setting: UserPrivacySetting
    rules: UserPrivacySettingRules
