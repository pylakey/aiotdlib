# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetGroupsInCommon(BaseObject):
    """
    Returns a list of common group chats with a given user. Chats are sorted by their type and creation date

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param offset_chat_id: Chat identifier starting from which to return chats; use 0 for the first request
    :type offset_chat_id: :class:`Int53`
    :param limit: The maximum number of chats to be returned; up to 100
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getGroupsInCommon"] = "getGroupsInCommon"
    user_id: Int53
    offset_chat_id: Int53
    limit: Int32
