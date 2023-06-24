# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetAnimatedEmoji(BaseObject):
    """
    Returns an animated emoji corresponding to a given emoji. Returns a 404 error if the emoji has no animated emoji

    :param emoji: The emoji
    :type emoji: :class:`String`
    """

    ID: typing.Literal["getAnimatedEmoji"] = "getAnimatedEmoji"
    emoji: String
