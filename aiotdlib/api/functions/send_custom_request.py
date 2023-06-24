# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SendCustomRequest(BaseObject):
    """
    Sends a custom request; for bots only

    :param method: The method name
    :type method: :class:`String`
    :param parameters: JSON-serialized method parameters
    :type parameters: :class:`String`
    """

    ID: typing.Literal["sendCustomRequest"] = "sendCustomRequest"
    method: String
    parameters: String
