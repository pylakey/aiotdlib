# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AddPendingPaidMessageReaction(BaseObject):
    """
    Adds the paid message reaction to a message. Use getMessageAvailableReactions to check whether the reaction is available for the message

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param star_count: Number of Telegram Stars to be used for the reaction. The total number of pending paid reactions must not exceed getOption("paid_reaction_star_count_max")
    :type star_count: :class:`Int53`
    :param use_default_is_anonymous: Pass true if the user didn't choose anonymity explicitly, for example, the reaction is set from the message bubble
    :type use_default_is_anonymous: :class:`Bool`
    :param is_anonymous: Pass true to make paid reaction of the user on the message anonymous; pass false to make the user's profile visible among top reactors. Ignored if use_default_is_anonymous == true
    :type is_anonymous: :class:`Bool`
    """

    ID: typing.Literal["addPendingPaidMessageReaction"] = Field(
        "addPendingPaidMessageReaction", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    message_id: Int53
    star_count: Int53
    use_default_is_anonymous: Bool = False
    is_anonymous: Bool = False
