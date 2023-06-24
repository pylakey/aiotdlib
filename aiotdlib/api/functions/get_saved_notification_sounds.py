# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSavedNotificationSounds(BaseObject):
    """
    Returns list of saved notification sounds. If a sound isn't in the list, then default sound needs to be used
    """

    ID: typing.Literal["getSavedNotificationSounds"] = "getSavedNotificationSounds"
