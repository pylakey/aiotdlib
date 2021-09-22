# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetFile(BaseObject):
    """
    Returns information about a file; this is an offline request
    
    :param file_id: Identifier of the file to get
    :type file_id: :class:`int`
    
    """

    ID: str = Field("getFile", alias="@type")
    file_id: int

    @staticmethod
    def read(q: dict) -> GetFile:
        return GetFile.construct(**q)
