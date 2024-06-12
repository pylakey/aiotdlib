# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AddQuickReplyShortcutInlineQueryResultMessage(BaseObject):
    """
    Adds a message to a quick reply shortcut via inline bot. If shortcut doesn't exist and there are less than getOption("quick_reply_shortcut_count_max") shortcuts, then a new shortcut is created. The shortcut must not contain more than getOption("quick_reply_shortcut_message_count_max") messages after adding the new message. Returns the added message

    :param shortcut_name: Name of the target shortcut
    :type shortcut_name: :class:`String`
    :param query_id: Identifier of the inline query
    :type query_id: :class:`Int64`
    :param result_id: Identifier of the inline query result
    :type result_id: :class:`String`
    :param reply_to_message_id: Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none
    :type reply_to_message_id: :class:`Int53`
    :param hide_via_bot: Pass true to hide the bot, via which the message is sent. Can be used only for bots getOption("animation_search_bot_username"), getOption("photo_search_bot_username"), and getOption("venue_search_bot_username")
    :type hide_via_bot: :class:`Bool`
    """

    ID: typing.Literal["addQuickReplyShortcutInlineQueryResultMessage"] = Field(
        "addQuickReplyShortcutInlineQueryResultMessage", validation_alias="@type", alias="@type"
    )
    shortcut_name: String
    query_id: Int64
    result_id: String
    reply_to_message_id: Int53 = 0
    hide_via_bot: Bool = False
