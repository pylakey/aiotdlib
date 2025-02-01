# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStarSubscriptions(BaseObject):
    """
    Returns the list of Telegram Star subscriptions for the current user

    :param offset: Offset of the first subscription to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param only_expiring: Pass true to receive only expiring subscriptions for which there are no enough Telegram Stars to extend
    :type only_expiring: :class:`Bool`
    """

    ID: typing.Literal["getStarSubscriptions"] = Field("getStarSubscriptions", validation_alias="@type", alias="@type")
    offset: String
    only_expiring: Bool = False
