# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class EndGroupCallScreenSharing(BaseObject):
    """
    Ends screen sharing in a joined group call
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
    """

    ID: str = Field("endGroupCallScreenSharing", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> EndGroupCallScreenSharing:
        return EndGroupCallScreenSharing.construct(**q)
