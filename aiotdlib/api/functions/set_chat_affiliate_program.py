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
    AffiliateProgramParameters,
)


class SetChatAffiliateProgram(BaseObject):
    """
    Changes affiliate program for a bot

    :param chat_id: Identifier of the chat with an owned bot for which affiliate program is changed
    :type chat_id: :class:`Int53`
    :param parameters: Parameters of the affiliate program; pass null to close the currently active program. If there is an active program, then commission and program duration can only be increased. If the active program is scheduled to be closed, then it can't be changed anymore, defaults to None
    :type parameters: :class:`AffiliateProgramParameters`, optional
    """

    ID: typing.Literal["setChatAffiliateProgram"] = Field(
        "setChatAffiliateProgram", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    parameters: typing.Optional[AffiliateProgramParameters] = None
