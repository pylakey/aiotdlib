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
)


class GetBlockedMessageSenders(BaseObject):
    """
    Returns users and chats that were blocked by the current user

    :param block_list: Block list from which to return users
    :type block_list: :class:`BlockList`
    :param offset: Number of users and chats to skip in the result; must be non-negative
    :type offset: :class:`Int32`
    :param limit: The maximum number of users and chats to return; up to 100
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getBlockedMessageSenders"] = "getBlockedMessageSenders"
    block_list: BlockList
    offset: Int32
    limit: Int32
