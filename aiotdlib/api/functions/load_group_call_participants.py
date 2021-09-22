# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class LoadGroupCallParticipants(BaseObject):
    """
    Loads more participants of a group call. The loaded participants will be received through updates. Use the field groupCall.loaded_all_participants to check whether all participants has already been loaded
    
    :param group_call_id: Group call identifier. The group call must be previously received through getGroupCall and must be joined or being joined
    :type group_call_id: :class:`int`
    
    :param limit: The maximum number of participants to load
    :type limit: :class:`int`
    
    """

    ID: str = Field("loadGroupCallParticipants", alias="@type")
    group_call_id: int
    limit: int

    @staticmethod
    def read(q: dict) -> LoadGroupCallParticipants:
        return LoadGroupCallParticipants.construct(**q)
