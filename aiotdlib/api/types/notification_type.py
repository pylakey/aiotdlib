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
    
    Params:
        call_id (:class:`int`)
            Call identifier
        
    """

    ID: str = Field("notificationTypeNewCall", alias="@type")
    call_id: int

    @staticmethod
    def read(q: dict) -> NotificationTypeNewCall:
        return NotificationTypeNewCall.construct(**q)


class NotificationTypeNewMessage(NotificationType):
    """
    New message was received
    
    Params:
        message (:class:`Message`)
            The message
        
    """

    ID: str = Field("notificationTypeNewMessage", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> NotificationTypeNewMessage:
        return NotificationTypeNewMessage.construct(**q)


class NotificationTypeNewPushMessage(NotificationType):
    """
    New message was received through a push notification
    
    Params:
        message_id (:class:`int`)
            The message identifier. The message will not be available in the chat history, but the ID can be used in viewMessages, or as reply_to_message_id
        
        sender (:class:`MessageSender`)
            The sender of the message. Corresponding user or chat may be inaccessible
        
        sender_name (:class:`str`)
            Name of the sender
        
        is_outgoing (:class:`bool`)
            True, if the message is outgoing
        
        content (:class:`PushMessageContent`)
            Push message content
        
    """

    ID: str = Field("notificationTypeNewPushMessage", alias="@type")
    message_id: int
    sender: MessageSender
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
