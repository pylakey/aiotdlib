# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetMessageFileType(BaseObject):
    """
    Returns information about a file with messages exported from another app
    
    :param message_file_head: Beginning of the message file; up to 100 first lines
    :type message_file_head: :class:`str`
    
    """

    ID: str = Field("getMessageFileType", alias="@type")
    message_file_head: str

    @staticmethod
    def read(q: dict) -> GetMessageFileType:
        return GetMessageFileType.construct(**q)
