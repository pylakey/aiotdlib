# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetSavedNotificationSound(BaseObject):
    """
    Returns saved notification sound by its identifier. Returns a 404 error if there is no saved notification sound with the specified identifier
    
    :param notification_sound_id: Identifier of the notification sound
    :type notification_sound_id: :class:`int`
    
    """

    ID: str = Field("getSavedNotificationSound", alias="@type")
    notification_sound_id: int

    @staticmethod
    def read(q: dict) -> GetSavedNotificationSound:
        return GetSavedNotificationSound.construct(**q)
