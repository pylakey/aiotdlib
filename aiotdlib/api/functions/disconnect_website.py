# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DisconnectWebsite(BaseObject):
    """
    Disconnects website from the current user's Telegram account

    :param website_id: Website identifier
    :type website_id: :class:`Int64`
    """

    ID: typing.Literal["disconnectWebsite"] = "disconnectWebsite"
    website_id: Int64
