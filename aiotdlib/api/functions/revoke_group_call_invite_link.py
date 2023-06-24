# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RevokeGroupCallInviteLink(BaseObject):
    """
    Revokes invite link for a group call. Requires groupCall.can_be_managed group call flag

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["revokeGroupCallInviteLink"] = "revokeGroupCallInviteLink"
    group_call_id: Int32
