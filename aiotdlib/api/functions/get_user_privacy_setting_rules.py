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
)


class GetUserPrivacySettingRules(BaseObject):
    """
    Returns the current privacy settings

    :param setting: The privacy setting
    :type setting: :class:`UserPrivacySetting`
    """

    ID: typing.Literal["getUserPrivacySettingRules"] = "getUserPrivacySettingRules"
    setting: UserPrivacySetting
