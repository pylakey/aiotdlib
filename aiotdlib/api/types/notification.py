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
    
    :param is_silent: True, if the notification was explicitly sent without sound
    :type is_silent: :class:`bool`
    
    :param type_: Notification type
    :type type_: :class:`NotificationType`
    
    """

    ID: str = Field("notification", alias="@type")
    id: int
    date: int
    is_silent: bool
    type_: NotificationType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> Notification:
        return Notification.construct(**q)
