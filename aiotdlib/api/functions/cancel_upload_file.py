# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CancelUploadFile(BaseObject):
    """
    Stops the uploading of a file. Supported only for files uploaded by using uploadFile. For other files the behavior is undefined
    
    :param file_id: Identifier of the file to stop uploading
    :type file_id: :class:`int`
    
    """

    ID: str = Field("cancelUploadFile", alias="@type")
    file_id: int

    @staticmethod
    def read(q: dict) -> CancelUploadFile:
        return CancelUploadFile.construct(**q)
