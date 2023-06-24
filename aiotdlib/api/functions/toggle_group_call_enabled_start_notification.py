# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleGroupCallEnabledStartNotification(BaseObject):
    """
    Toggles whether the current user will receive a notification when the group call will start; scheduled group calls only

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param enabled_start_notification: New value of the enabled_start_notification setting
    :type enabled_start_notification: :class:`Bool`
    """

    ID: typing.Literal["toggleGroupCallEnabledStartNotification"] = "toggleGroupCallEnabledStartNotification"
    group_call_id: Int32
    enabled_start_notification: Bool
