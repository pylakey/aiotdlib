# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class LoadGroupCallParticipants(BaseObject):
    """
    Loads more participants of a group call. The loaded participants will be received through updates. Use the field groupCall.loaded_all_participants to check whether all participants have already been loaded

    :param group_call_id: Group call identifier. The group call must be previously received through getGroupCall and must be joined or being joined
    :type group_call_id: :class:`Int32`
    :param limit: The maximum number of participants to load; up to 100
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["loadGroupCallParticipants"] = "loadGroupCallParticipants"
    group_call_id: Int32
    limit: Int32
