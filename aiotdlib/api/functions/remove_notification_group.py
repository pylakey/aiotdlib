# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RemoveNotificationGroup(BaseObject):
    """
    Removes a group of active notifications. Needs to be called only if the notification group is removed by the current user
    
    Params:
        notification_group_id (:class:`int`)
            Notification group identifier
        
        max_notification_id (:class:`int`)
            The maximum identifier of removed notifications
        
    """

    ID: str = Field("removeNotificationGroup", alias="@type")
    notification_group_id: int
    max_notification_id: int

    @staticmethod
    def read(q: dict) -> RemoveNotificationGroup:
        return RemoveNotificationGroup.construct(**q)
