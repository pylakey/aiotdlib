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
    InputMessageContent,
)


class AddQuickReplyShortcutMessageAlbum(BaseObject):
    """
    Adds 2-10 messages grouped together into an album to a quick reply shortcut. Currently, only audio, document, photo and video messages can be grouped into an album. Documents and audio files can be only grouped in an album with messages of the same type. Returns sent messages

    :param shortcut_name: Name of the target shortcut
    :type shortcut_name: :class:`String`
    :param input_message_contents: Contents of messages to be sent. At most 10 messages can be added to an album. All messages must have the same value of show_caption_above_media
    :type input_message_contents: :class:`Vector[InputMessageContent]`
    :param reply_to_message_id: Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none
    :type reply_to_message_id: :class:`Int53`
    """

    ID: typing.Literal["addQuickReplyShortcutMessageAlbum"] = Field(
        "addQuickReplyShortcutMessageAlbum", validation_alias="@type", alias="@type"
    )
    shortcut_name: String
    input_message_contents: Vector[InputMessageContent]
    reply_to_message_id: Int53 = 0
