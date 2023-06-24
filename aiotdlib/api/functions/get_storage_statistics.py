# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStorageStatistics(BaseObject):
    """
    Returns storage usage statistics. Can be called before authorization

    :param chat_limit: The maximum number of chats with the largest storage usage for which separate statistics need to be returned. All other chats will be grouped in entries with chat_id == 0. If the chat info database is not used, the chat_limit is ignored and is always set to 0
    :type chat_limit: :class:`Int32`
    """

    ID: typing.Literal["getStorageStatistics"] = "getStorageStatistics"
    chat_limit: Int32
