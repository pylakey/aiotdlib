# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteBotMediaPreviews(BaseObject):
    """
    Delete media previews from the list of media previews of a bot

    :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
    :type bot_user_id: :class:`Int53`
    :param language_code: Language code of the media previews to delete
    :type language_code: :class:`String`
    :param file_ids: File identifiers of the media to delete
    :type file_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["deleteBotMediaPreviews"] = Field(
        "deleteBotMediaPreviews", validation_alias="@type", alias="@type"
    )
    bot_user_id: Int53
    language_code: String
    file_ids: Vector[Int32]
