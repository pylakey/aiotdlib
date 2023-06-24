# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPushReceiverId(BaseObject):
    """
    Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification. Can be called synchronously

    :param payload: JSON-encoded push notification payload
    :type payload: :class:`String`
    """

    ID: typing.Literal["getPushReceiverId"] = "getPushReceiverId"
    payload: String
