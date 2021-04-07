# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RemoveNotification(BaseObject):
    """
    Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user
    
    Params:
        notification_group_id (:class:`int`)
            Identifier of notification group to which the notification belongs
        
        notification_id (:class:`int`)
            Identifier of removed notification
        
    """

    ID: str = Field("removeNotification", alias="@type")
    notification_group_id: int
    notification_id: int

    @staticmethod
    def read(q: dict) -> RemoveNotification:
        return RemoveNotification.construct(**q)
