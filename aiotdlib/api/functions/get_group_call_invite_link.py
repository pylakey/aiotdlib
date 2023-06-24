# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetGroupCallInviteLink(BaseObject):
    """
    Returns invite link to a video chat in a public chat

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param can_self_unmute: Pass true if the invite link needs to contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselves. Requires groupCall.can_be_managed group call flag
    :type can_self_unmute: :class:`Bool`
    """

    ID: typing.Literal["getGroupCallInviteLink"] = "getGroupCallInviteLink"
    group_call_id: Int32
    can_self_unmute: Bool = False
