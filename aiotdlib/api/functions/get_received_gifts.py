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
    MessageSender,
)


class GetReceivedGifts(BaseObject):
    """
    Returns gifts received by the given user or chat

    :param owner_id: Identifier of the gift receiver
    :type owner_id: :class:`MessageSender`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of gifts to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    :param exclude_unsaved: Pass true to exclude gifts that aren't saved to the chat's profile page. Always true for gifts received by other users and channel chats without can_post_messages administrator right
    :type exclude_unsaved: :class:`Bool`
    :param exclude_saved: Pass true to exclude gifts that are saved to the chat's profile page. Always false for gifts received by other users and channel chats without can_post_messages administrator right
    :type exclude_saved: :class:`Bool`
    :param exclude_unlimited: Pass true to exclude gifts that can be purchased unlimited number of times
    :type exclude_unlimited: :class:`Bool`
    :param exclude_limited: Pass true to exclude gifts that can be purchased limited number of times
    :type exclude_limited: :class:`Bool`
    :param exclude_upgraded: Pass true to exclude upgraded gifts
    :type exclude_upgraded: :class:`Bool`
    :param sort_by_price: Pass true to sort results by gift price instead of send date
    :type sort_by_price: :class:`Bool`
    """

    ID: typing.Literal["getReceivedGifts"] = Field("getReceivedGifts", validation_alias="@type", alias="@type")
    owner_id: MessageSender
    offset: String
    limit: Int32
    exclude_unsaved: Bool = False
    exclude_saved: Bool = False
    exclude_unlimited: Bool = False
    exclude_limited: Bool = False
    exclude_upgraded: Bool = False
    sort_by_price: Bool = False
