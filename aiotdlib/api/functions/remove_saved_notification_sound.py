# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RemoveSavedNotificationSound(BaseObject):
    """
    Removes a notification sound from the list of saved notification sounds
    
    :param notification_sound_id: Identifier of the notification sound
    :type notification_sound_id: :class:`int`
    
    """

    ID: str = Field("removeSavedNotificationSound", alias="@type")
    notification_sound_id: int

    @staticmethod
    def read(q: dict) -> RemoveSavedNotificationSound:
        return RemoveSavedNotificationSound.construct(**q)
