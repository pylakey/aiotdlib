# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .notification import Notification
from .notification_group_type import NotificationGroupType
from ..base_object import BaseObject


class NotificationGroup(BaseObject):
    """
    Describes a group of notifications
    
    Params:
        id (:class:`int`)
            Unique persistent auto-incremented from 1 identifier of the notification group
        
        type_ (:class:`NotificationGroupType`)
            Type of the group
        
        chat_id (:class:`int`)
            Identifier of a chat to which all notifications in the group belong
        
        total_count (:class:`int`)
            Total number of active notifications in the group
        
        notifications (:obj:`list[Notification]`)
            The list of active notifications
        
    """

    ID: str = Field("notificationGroup", alias="@type")
    id: int
    type_: NotificationGroupType = Field(..., alias='type')
    chat_id: int
    total_count: int
    notifications: list[Notification]

    @staticmethod
    def read(q: dict) -> NotificationGroup:
        return NotificationGroup.construct(**q)
