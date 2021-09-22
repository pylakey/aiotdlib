# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RemoveNotification(BaseObject):
    """
    Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user
    
    :param notification_group_id: Identifier of notification group to which the notification belongs
    :type notification_group_id: :class:`int`
    
    :param notification_id: Identifier of removed notification
    :type notification_id: :class:`int`
    
    """

    ID: str = Field("removeNotification", alias="@type")
    notification_group_id: int
    notification_id: int

    @staticmethod
    def read(q: dict) -> RemoveNotification:
        return RemoveNotification.construct(**q)
