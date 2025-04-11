# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetWebAppPlaceholder(BaseObject):
    """
    Returns a default placeholder for Web Apps of a bot. This is an offline method. Returns a 404 error if the placeholder isn't known

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["getWebAppPlaceholder"] = Field("getWebAppPlaceholder", validation_alias="@type", alias="@type")
    bot_user_id: Int53
