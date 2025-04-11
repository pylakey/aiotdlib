# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStickerOutline(BaseObject):
    """
    Returns outline of a sticker. This is an offline method. Returns a 404 error if the outline isn't known

    :param sticker_file_id: File identifier of the sticker
    :type sticker_file_id: :class:`Int32`
    :param for_animated_emoji: Pass true to get the outline scaled for animated emoji
    :type for_animated_emoji: :class:`Bool`
    :param for_clicked_animated_emoji_message: Pass true to get the outline scaled for clicked animated emoji message
    :type for_clicked_animated_emoji_message: :class:`Bool`
    """

    ID: typing.Literal["getStickerOutline"] = Field("getStickerOutline", validation_alias="@type", alias="@type")
    sticker_file_id: Int32
    for_animated_emoji: Bool = False
    for_clicked_animated_emoji_message: Bool = False
