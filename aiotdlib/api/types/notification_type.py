# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message import Message
from .message_sender import MessageSender
from .push_message_content import PushMessageContent
from ..base_object import BaseObject


class NotificationType(BaseObject):
    """
    Contains detailed information about a notification
    
    """

    ID: str = Field("notificationType", alias="@type")


class NotificationTypeNewCall(NotificationType):
    """
    New call was received
    
    :param call_id: Call identifier
    :type call_id: :class:`int`
    
    """

    ID: str = Field("notificationTypeNewCall", alias="@type")
    call_id: int

    @staticmethod
    def read(q: dict) -> NotificationTypeNewCall:
        return NotificationTypeNewCall.construct(**q)


class NotificationTypeNewMessage(NotificationType):
    """
    New message was received
    
    :param message: The message
    :type message: :class:`Message`
    
    :param show_preview: True, if message content must be displayed in notifications
    :type show_preview: :class:`bool`
    
    """

    ID: str = Field("notificationTypeNewMessage", alias="@type")
    message: Message
    show_preview: bool

    @staticmethod
    def read(q: dict) -> NotificationTypeNewMessage:
        return NotificationTypeNewMessage.construct(**q)


class NotificationTypeNewPushMessage(NotificationType):
    """
    New message was received through a push notification
    
    :param message_id: The message identifier. The message will not be available in the chat history, but the ID can be used in viewMessages, or as reply_to_message_id
    :type message_id: :class:`int`
    
    :param sender_id: Identifier of the sender of the message. Corresponding user or chat may be inaccessible
    :type sender_id: :class:`MessageSender`
    
    :param sender_name: Name of the sender
    :type sender_name: :class:`str`
    
    :param is_outgoing: True, if the message is outgoing
    :type is_outgoing: :class:`bool`
    
    :param content: Push message content
    :type content: :class:`PushMessageContent`
    
    """

    ID: str = Field("notificationTypeNewPushMessage", alias="@type")
    message_id: int
    sender_id: MessageSender
    sender_name: str
    is_outgoing: bool
    content: PushMessageContent

    @staticmethod
    def read(q: dict) -> NotificationTypeNewPushMessage:
        return NotificationTypeNewPushMessage.construct(**q)


class NotificationTypeNewSecretChat(NotificationType):
    """
    New secret chat was created
    
    """

    ID: str = Field("notificationTypeNewSecretChat", alias="@type")

    @staticmethod
    def read(q: dict) -> NotificationTypeNewSecretChat:
        return NotificationTypeNewSecretChat.construct(**q)
