# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class AddSavedNotificationSound(BaseObject):
    """
    Adds a new notification sound to the list of saved notification sounds. The new notification sound is added to the top of the list. If it is already in the list, its position isn't changed
    
    :param sound: Notification sound file to add
    :type sound: :class:`InputFile`
    
    """

    ID: str = Field("addSavedNotificationSound", alias="@type")
    sound: InputFile

    @staticmethod
    def read(q: dict) -> AddSavedNotificationSound:
        return AddSavedNotificationSound.construct(**q)
