# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    MessageSendOptions,
)


class ForwardMessages(BaseObject):
    """
    Forwards previously sent messages. Returns the forwarded messages in the same order as the message identifiers passed in message_ids. If a message can't be forwarded, null will be returned instead of the message

    :param chat_id: Identifier of the chat to which to forward messages
    :type chat_id: :class:`Int53`
    :param from_chat_id: Identifier of the chat from which to forward messages
    :type from_chat_id: :class:`Int53`
    :param message_ids: Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order. At most 100 messages can be forwarded simultaneously
    :type message_ids: :class:`Vector[Int53]`
    :param message_thread_id: If not 0, a message thread identifier in which the message will be sent; for forum threads only
    :type message_thread_id: :class:`Int53`
    :param send_copy: Pass true to copy content of the messages without reference to the original sender. Always true if the messages are forwarded to a secret chat or are local
    :type send_copy: :class:`Bool`
    :param remove_caption: Pass true to remove media captions of message copies. Ignored if send_copy is false
    :type remove_caption: :class:`Bool`
    :param only_preview: Pass true to get fake messages instead of actually forwarding them
    :type only_preview: :class:`Bool`
    :param options: Options to be used to send the messages; pass null to use default options, defaults to None
    :type options: :class:`MessageSendOptions`, optional
    """

    ID: typing.Literal["forwardMessages"] = "forwardMessages"
    chat_id: Int53
    from_chat_id: Int53
    message_ids: Vector[Int53]
    message_thread_id: Int53 = 0
    send_copy: Bool = False
    remove_caption: Bool = False
    only_preview: Bool = False
    options: typing.Optional[MessageSendOptions] = None
