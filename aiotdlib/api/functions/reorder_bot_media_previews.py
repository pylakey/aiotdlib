# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReorderBotMediaPreviews(BaseObject):
    """
    Changes order of media previews in the list of media previews of a bot

    :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
    :type bot_user_id: :class:`Int53`
    :param language_code: Language code of the media previews to reorder
    :type language_code: :class:`String`
    :param file_ids: File identifiers of the media in the new order
    :type file_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["reorderBotMediaPreviews"] = Field(
        "reorderBotMediaPreviews", validation_alias="@type", alias="@type"
    )
    bot_user_id: Int53
    language_code: String
    file_ids: Vector[Int32]
