# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class WriteGeneratedFilePart(BaseObject):
    """
    Writes a part of a generated file. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file
    
    :param generation_id: The identifier of the generation process
    :type generation_id: :class:`int`
    
    :param offset: The offset from which to write the data to the file
    :type offset: :class:`int`
    
    :param data: The data to write
    :type data: :class:`str`
    
    """

    ID: str = Field("writeGeneratedFilePart", alias="@type")
    generation_id: int
    offset: int
    data: str

    @staticmethod
    def read(q: dict) -> WriteGeneratedFilePart:
        return WriteGeneratedFilePart.construct(**q)
