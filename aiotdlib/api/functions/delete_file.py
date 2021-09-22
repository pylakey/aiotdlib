# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class DeleteFile(BaseObject):
    """
    Deletes a file from the TDLib file cache
    
    :param file_id: Identifier of the file to delete
    :type file_id: :class:`int`
    
    """

    ID: str = Field("deleteFile", alias="@type")
    file_id: int

    @staticmethod
    def read(q: dict) -> DeleteFile:
        return DeleteFile.construct(**q)
