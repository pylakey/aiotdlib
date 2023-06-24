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


class SetBotProfilePhoto(BaseObject):
    """
    Changes a profile photo for a bot

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param photo: Profile photo to set; pass null to delete the chat photo, defaults to None
    :type photo: :class:`InputChatPhoto`, optional
    """

    ID: typing.Literal["setBotProfilePhoto"] = "setBotProfilePhoto"
    bot_user_id: Int53
    photo: typing.Optional[InputChatPhoto] = None
