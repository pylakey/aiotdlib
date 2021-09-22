# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RemoveNotificationGroup(BaseObject):
    """
    Removes a group of active notifications. Needs to be called only if the notification group is removed by the current user
    
    :param notification_group_id: Notification group identifier
    :type notification_group_id: :class:`int`
    
    :param max_notification_id: The maximum identifier of removed notifications
    :type max_notification_id: :class:`int`
    
    """

    ID: str = Field("removeNotificationGroup", alias="@type")
    notification_group_id: int
    max_notification_id: int

    @staticmethod
    def read(q: dict) -> RemoveNotificationGroup:
        return RemoveNotificationGroup.construct(**q)
