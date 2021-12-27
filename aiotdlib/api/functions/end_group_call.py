# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class EndGroupCall(BaseObject):
    """
    Ends a group call. Requires groupCall.can_be_managed
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    """

    ID: str = Field("endGroupCall", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> EndGroupCall:
        return EndGroupCall.construct(**q)
