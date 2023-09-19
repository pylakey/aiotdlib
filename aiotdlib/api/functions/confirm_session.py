# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ConfirmSession(BaseObject):
    """
    Confirms an unconfirmed session of the current user from another device

    :param session_id: Session identifier
    :type session_id: :class:`Int64`
    """

    ID: typing.Literal["confirmSession"] = "confirmSession"
    session_id: Int64
