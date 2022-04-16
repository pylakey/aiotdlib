# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .notification_type import NotificationType
from ..base_object import BaseObject


class Notification(BaseObject):
    """
    Contains information about a notification
    
    :param id: Unique persistent identifier of this notification
    :type id: :class:`int`
    
    :param date: Notification date
    :type date: :class:`int`
    
    :param sound_id: Identifier of the notification sound to be played; 0 if sound is disabled
    :type sound_id: :class:`int`
    
    :param type_: Notification type
    :type type_: :class:`NotificationType`
    
    """

    ID: str = Field("notification", alias="@type")
    id: int
    date: int
    sound_id: int
    type_: NotificationType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> Notification:
        return Notification.construct(**q)
