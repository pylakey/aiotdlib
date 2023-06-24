# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetInactiveSessionTtl(BaseObject):
    """
    Changes the period of inactivity after which sessions will automatically be terminated

    :param inactive_session_ttl_days: New number of days of inactivity before sessions will be automatically terminated; 1-366 days
    :type inactive_session_ttl_days: :class:`Int32`
    """

    ID: typing.Literal["setInactiveSessionTtl"] = "setInactiveSessionTtl"
    inactive_session_ttl_days: Int32
