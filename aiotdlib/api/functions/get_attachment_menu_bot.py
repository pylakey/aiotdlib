# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetAttachmentMenuBot(BaseObject):
    """
    Returns information about a bot that can be added to attachment or side menu

    :param bot_user_id: Bot's user identifier
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["getAttachmentMenuBot"] = "getAttachmentMenuBot"
    bot_user_id: Int53
