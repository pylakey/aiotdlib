# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .notification_sound import NotificationSound
from ..base_object import BaseObject


class NotificationSounds(BaseObject):
    """
    Contains a list of notification sounds
    
    :param notification_sounds: A list of notification sounds
    :type notification_sounds: :class:`list[NotificationSound]`
    
    """

    ID: str = Field("notificationSounds", alias="@type")
    notification_sounds: list[NotificationSound]

    @staticmethod
    def read(q: dict) -> NotificationSounds:
        return NotificationSounds.construct(**q)
