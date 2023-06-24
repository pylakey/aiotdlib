# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteMessages(BaseObject):
    """
    Deletes messages

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_ids: Identifiers of the messages to be deleted
    :type message_ids: :class:`Vector[Int53]`
    :param revoke: Pass true to delete messages for all chat members. Always true for supergroups, channels and secret chats
    :type revoke: :class:`Bool`
    """

    ID: typing.Literal["deleteMessages"] = "deleteMessages"
    chat_id: Int53
    message_ids: Vector[Int53]
    revoke: Bool = False
