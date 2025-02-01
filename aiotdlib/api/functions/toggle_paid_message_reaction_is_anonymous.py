# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class TogglePaidMessageReactionIsAnonymous(BaseObject):
    """
    Changes whether the paid message reaction of the user to a message is anonymous. The message must have paid reaction added by the user

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param is_anonymous: Pass true to make paid reaction of the user on the message anonymous; pass false to make the user's profile visible among top reactors
    :type is_anonymous: :class:`Bool`
    """

    ID: typing.Literal["togglePaidMessageReactionIsAnonymous"] = Field(
        "togglePaidMessageReactionIsAnonymous", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    message_id: Int53
    is_anonymous: Bool = False
