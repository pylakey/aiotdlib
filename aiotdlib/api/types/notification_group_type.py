# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class NotificationGroupType(BaseObject):
    """
    Describes the type of notifications in a notification group
    
    """

    ID: str = Field("notificationGroupType", alias="@type")


class NotificationGroupTypeCalls(NotificationGroupType):
    """
    A group containing notifications of type notificationTypeNewCall
    
    """

    ID: str = Field("notificationGroupTypeCalls", alias="@type")

    @staticmethod
    def read(q: dict) -> NotificationGroupTypeCalls:
        return NotificationGroupTypeCalls.construct(**q)


class NotificationGroupTypeMentions(NotificationGroupType):
    """
    A group containing notifications of type notificationTypeNewMessage and notificationTypeNewPushMessage with unread mentions of the current user, replies to their messages, or a pinned message
    
    """

    ID: str = Field("notificationGroupTypeMentions", alias="@type")

    @staticmethod
    def read(q: dict) -> NotificationGroupTypeMentions:
        return NotificationGroupTypeMentions.construct(**q)


class NotificationGroupTypeMessages(NotificationGroupType):
    """
    A group containing notifications of type notificationTypeNewMessage and notificationTypeNewPushMessage with ordinary unread messages
    
    """

    ID: str = Field("notificationGroupTypeMessages", alias="@type")

    @staticmethod
    def read(q: dict) -> NotificationGroupTypeMessages:
        return NotificationGroupTypeMessages.construct(**q)


class NotificationGroupTypeSecretChat(NotificationGroupType):
    """
    A group containing a notification of type notificationTypeNewSecretChat
    
    """

    ID: str = Field("notificationGroupTypeSecretChat", alias="@type")

    @staticmethod
    def read(q: dict) -> NotificationGroupTypeSecretChat:
        return NotificationGroupTypeSecretChat.construct(**q)
