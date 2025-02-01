# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClickChatSponsoredMessage(BaseObject):
    """
    Informs TDLib that the user opened the sponsored chat via the button, the name, the chat photo, a mention in the sponsored message text, or the media in the sponsored message

    :param chat_id: Chat identifier of the sponsored message
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the sponsored message
    :type message_id: :class:`Int53`
    :param is_media_click: Pass true if the media was clicked in the sponsored message
    :type is_media_click: :class:`Bool`
    :param from_fullscreen: Pass true if the user expanded the video from the sponsored message fullscreen before the click
    :type from_fullscreen: :class:`Bool`
    """

    ID: typing.Literal["clickChatSponsoredMessage"] = Field(
        "clickChatSponsoredMessage", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    message_id: Int53
    is_media_click: Bool = False
    from_fullscreen: Bool = False
