# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetEmojiReaction(BaseObject):
    """
    Returns information about a emoji reaction. Returns a 404 error if the reaction is not found

    :param emoji: Text representation of the reaction
    :type emoji: :class:`String`
    """

    ID: typing.Literal["getEmojiReaction"] = "getEmojiReaction"
    emoji: String
