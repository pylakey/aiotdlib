# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .file import File
from ..base_object import BaseObject


class NotificationSound(BaseObject):
    """
    Describes a notification sound in MP3 format
    
    :param id: Unique identifier of the notification sound
    :type id: :class:`int`
    
    :param duration: Duration of the sound, in seconds
    :type duration: :class:`int`
    
    :param date: Point in time (Unix timestamp) when the sound was created
    :type date: :class:`int`
    
    :param title: Title of the notification sound
    :type title: :class:`str`
    
    :param data: Arbitrary data, defined while the sound was uploaded
    :type data: :class:`str`
    
    :param sound: File containing the sound
    :type sound: :class:`File`
    
    """

    ID: str = Field("notificationSound", alias="@type")
    id: int
    duration: int
    date: int
    title: str
    data: str
    sound: File

    @staticmethod
    def read(q: dict) -> NotificationSound:
        return NotificationSound.construct(**q)
