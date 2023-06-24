# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class TerminateSession(BaseObject):
    """
    Terminates a session of the current user

    :param session_id: Session identifier
    :type session_id: :class:`Int64`
    """

    ID: typing.Literal["terminateSession"] = "terminateSession"
    session_id: Int64
