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
    Sends debug information for a call to Telegram servers
    
    :param call_id: Call identifier
    :type call_id: :class:`int`
    
    :param debug_information: Debug information in application-specific format
    :type debug_information: :class:`str`
    
    """

    ID: str = Field("sendCallDebugInformation", alias="@type")
    call_id: int
    debug_information: str

    @staticmethod
    def read(q: dict) -> SendCallDebugInformation:
        return SendCallDebugInformation.construct(**q)
