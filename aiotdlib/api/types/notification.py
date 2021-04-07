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
    
    Params:
        id (:class:`int`)
            Unique persistent identifier of this notification
        
        date (:class:`int`)
            Notification date
        
        is_silent (:class:`bool`)
            True, if the notification was initially silent
        
        type_ (:class:`NotificationType`)
            Notification type
        
    """

    ID: str = Field("notification", alias="@type")
    id: int
    date: int
    is_silent: bool
    type_: NotificationType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> Notification:
        return Notification.construct(**q)
