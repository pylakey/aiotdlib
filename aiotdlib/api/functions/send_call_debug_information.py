# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SendCallDebugInformation(BaseObject):
    """
    Sends debug information for a call
    
    Params:
        call_id (:class:`int`)
            Call identifier
        
        debug_information (:class:`str`)
            Debug information in application-specific format
        
    """

    ID: str = Field("sendCallDebugInformation", alias="@type")
    call_id: int
    debug_information: str

    @staticmethod
    def read(q: dict) -> SendCallDebugInformation:
        return SendCallDebugInformation.construct(**q)
