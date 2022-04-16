# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSendOptions


class ForwardMessages(BaseObject):
    """
    Forwards previously sent messages. Returns the forwarded messages in the same order as the message identifiers passed in message_ids. If a message can't be forwarded, null will be returned instead of the message
    
    :param chat_id: Identifier of the chat to which to forward messages
    :type chat_id: :class:`int`
    
    :param from_chat_id: Identifier of the chat from which to forward messages
    :type from_chat_id: :class:`int`
    
    :param message_ids: Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order. At most 100 messages can be forwarded simultaneously
    :type message_ids: :class:`list[int]`
    
    :param options: Options to be used to send the messages; pass null to use default options
    :type options: :class:`MessageSendOptions`
    
    :param send_copy: Pass true to copy content of the messages without reference to the original sender. Always true if the messages are forwarded to a secret chat or are local
    :type send_copy: :class:`bool`
    
    :param remove_caption: Pass true to remove media captions of message copies. Ignored if send_copy is false
    :type remove_caption: :class:`bool`
    
    :param only_preview: Pass true to get fake messages instead of actually forwarding them
    :type only_preview: :class:`bool`
    
    """

    ID: str = Field("forwardMessages", alias="@type")
    chat_id: int
    from_chat_id: int
    message_ids: list[int]
    options: MessageSendOptions
    send_copy: bool
    remove_caption: bool
    only_preview: bool

    @staticmethod
    def read(q: dict) -> ForwardMessages:
        return ForwardMessages.construct(**q)
