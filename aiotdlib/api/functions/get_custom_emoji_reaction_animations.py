# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetCustomEmojiReactionAnimations(BaseObject):
    """
    Returns TGS stickers with generic animations for custom emoji reactions
    """

    ID: typing.Literal["getCustomEmojiReactionAnimations"] = "getCustomEmojiReactionAnimations"
