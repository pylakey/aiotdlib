# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class SendCallLog(BaseObject):
    """
    Sends log file for a call to Telegram servers
    
    :param call_id: Call identifier
    :type call_id: :class:`int`
    
    :param log_file: Call log file. Only inputFileLocal and inputFileGenerated are supported
    :type log_file: :class:`InputFile`
    
    """

    ID: str = Field("sendCallLog", alias="@type")
    call_id: int
    log_file: InputFile

    @staticmethod
    def read(q: dict) -> SendCallLog:
        return SendCallLog.construct(**q)
