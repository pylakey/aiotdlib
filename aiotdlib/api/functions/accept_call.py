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
    CallProtocol,
)


class AcceptCall(BaseObject):
    """
    Accepts an incoming call

    :param call_id: Call identifier
    :type call_id: :class:`Int32`
    :param protocol: The call protocols supported by the application
    :type protocol: :class:`CallProtocol`
    """

    ID: typing.Literal["acceptCall"] = "acceptCall"
    call_id: Int32
    protocol: CallProtocol
