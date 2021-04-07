# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class MessageForwardOrigin(BaseObject):
    """
    Contains information about the origin of a forwarded message
    
    """

    ID: str = Field("messageForwardOrigin", alias="@type")


class MessageForwardOriginChannel(MessageForwardOrigin):
    """
    The message was originally a post in a channel
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat from which the message was originally forwarded
        
        message_id (:class:`int`)
            Message identifier of the original message
        
        author_signature (:class:`str`)
            Original post author signature
        
    """

    ID: str = Field("messageForwardOriginChannel", alias="@type")
    chat_id: int
    message_id: int
    author_signature: str

    @staticmethod
    def read(q: dict) -> MessageForwardOriginChannel:
        return MessageForwardOriginChannel.construct(**q)


class MessageForwardOriginChat(MessageForwardOrigin):
    """
    The message was originally sent by an anonymous chat administrator on behalf of the chat
    
    Params:
        sender_chat_id (:class:`int`)
            Identifier of the chat that originally sent the message
        
        author_signature (:class:`str`)
            Original message author signature
        
    """

    ID: str = Field("messageForwardOriginChat", alias="@type")
    sender_chat_id: int
    author_signature: str

    @staticmethod
    def read(q: dict) -> MessageForwardOriginChat:
        return MessageForwardOriginChat.construct(**q)


class MessageForwardOriginHiddenUser(MessageForwardOrigin):
    """
    The message was originally sent by a user, which is hidden by their privacy settings
    
    Params:
        sender_name (:class:`str`)
            Name of the sender
        
    """

    ID: str = Field("messageForwardOriginHiddenUser", alias="@type")
    sender_name: str

    @staticmethod
    def read(q: dict) -> MessageForwardOriginHiddenUser:
        return MessageForwardOriginHiddenUser.construct(**q)


class MessageForwardOriginMessageImport(MessageForwardOrigin):
    """
    The message was imported from an exported message history
    
    Params:
        sender_name (:class:`str`)
            Name of the sender
        
    """

    ID: str = Field("messageForwardOriginMessageImport", alias="@type")
    sender_name: str

    @staticmethod
    def read(q: dict) -> MessageForwardOriginMessageImport:
        return MessageForwardOriginMessageImport.construct(**q)


class MessageForwardOriginUser(MessageForwardOrigin):
    """
    The message was originally sent by a known user
    
    Params:
        sender_user_id (:class:`int`)
            Identifier of the user that originally sent the message
        
    """

    ID: str = Field("messageForwardOriginUser", alias="@type")
    sender_user_id: int

    @staticmethod
    def read(q: dict) -> MessageForwardOriginUser:
        return MessageForwardOriginUser.construct(**q)
