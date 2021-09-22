# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .notification import Notification
from .notification_group_type import NotificationGroupType
from ..base_object import BaseObject


class NotificationGroup(BaseObject):
    """
    Describes a group of notifications
    
    :param id: Unique persistent auto-incremented from 1 identifier of the notification group
    :type id: :class:`int`
    
    :param type_: Type of the group
    :type type_: :class:`NotificationGroupType`
    
    :param chat_id: Identifier of a chat to which all notifications in the group belong
    :type chat_id: :class:`int`
    
    :param total_count: Total number of active notifications in the group
    :type total_count: :class:`int`
    
    :param notifications: The list of active notifications
    :type notifications: :class:`list[Notification]`
    
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
