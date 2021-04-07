# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessageFileType(BaseObject):
    """
    Returns information about a file with messages exported from another app
    
    Params:
        message_file_head (:class:`str`)
            Beginning of the message file; up to 100 first lines
        
    """

    ID: str = Field("getMessageFileType", alias="@type")
    message_file_head: str

    @staticmethod
    def read(q: dict) -> GetMessageFileType:
        return GetMessageFileType.construct(**q)
