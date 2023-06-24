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
    InputChatPhoto,
)


class SetChatPhoto(BaseObject):
    """
    Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param photo: New chat photo; pass null to delete the chat photo, defaults to None
    :type photo: :class:`InputChatPhoto`, optional
    """

    ID: typing.Literal["setChatPhoto"] = "setChatPhoto"
    chat_id: Int53
    photo: typing.Optional[InputChatPhoto] = None
