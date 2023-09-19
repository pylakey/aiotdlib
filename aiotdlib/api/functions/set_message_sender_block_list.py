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
    BlockList,
    MessageSender,
)


class SetMessageSenderBlockList(BaseObject):
    """
    Changes the block list of a message sender. Currently, only users and supergroup chats can be blocked

    :param sender_id: Identifier of a message sender to block/unblock
    :type sender_id: :class:`MessageSender`
    :param block_list: New block list for the message sender; pass null to unblock the message sender, defaults to None
    :type block_list: :class:`BlockList`, optional
    """

    ID: typing.Literal["setMessageSenderBlockList"] = "setMessageSenderBlockList"
    sender_id: MessageSender
    block_list: typing.Optional[BlockList] = None
