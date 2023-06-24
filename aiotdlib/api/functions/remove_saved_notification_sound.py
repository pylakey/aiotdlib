# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveSavedNotificationSound(BaseObject):
    """
    Removes a notification sound from the list of saved notification sounds

    :param notification_sound_id: Identifier of the notification sound
    :type notification_sound_id: :class:`Int64`
    """

    ID: typing.Literal["removeSavedNotificationSound"] = "removeSavedNotificationSound"
    notification_sound_id: Int64
