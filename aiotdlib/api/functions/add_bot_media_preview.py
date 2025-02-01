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
    InputStoryContent,
)


class AddBotMediaPreview(BaseObject):
    """
    Adds a new media preview to the beginning of the list of media previews of a bot. Returns the added preview after addition is completed server-side. The total number of previews must not exceed getOption("bot_media_preview_count_max") for the given language

    :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
    :type bot_user_id: :class:`Int53`
    :param content: Content of the added preview
    :type content: :class:`InputStoryContent`
    :param language_code: A two-letter ISO 639-1 language code for which preview is added. If empty, then the preview will be shown to all users for whose languages there are no dedicated previews. If non-empty, then there must be an official language pack of the same name, which is returned by getLocalizationTargetInfo
    :type language_code: :class:`String`
    """

    ID: typing.Literal["addBotMediaPreview"] = Field("addBotMediaPreview", validation_alias="@type", alias="@type")
    bot_user_id: Int53
    content: InputStoryContent
    language_code: String = ""
