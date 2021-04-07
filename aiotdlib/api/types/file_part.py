# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class FilePart(BaseObject):
    """
    Contains a part of a file
    
    Params:
        data (:class:`str`)
            File bytes
        
    """

    ID: str = Field("filePart", alias="@type")
    data: str

    @staticmethod
    def read(q: dict) -> FilePart:
        return FilePart.construct(**q)
