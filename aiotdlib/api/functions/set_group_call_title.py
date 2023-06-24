# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetGroupCallTitle(BaseObject):
    """
    Sets group call title. Requires groupCall.can_be_managed group call flag

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param title: New group call title; 1-64 characters
    :type title: :class:`String`
    """

    ID: typing.Literal["setGroupCallTitle"] = "setGroupCallTitle"
    group_call_id: Int32
    title: String = Field(..., min_length=1, max_length=64)
