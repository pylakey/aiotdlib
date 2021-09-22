# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from ..base_object import BaseObject


class DatedFile(BaseObject):
    """
    File with the date it was uploaded
    
    :param file: The file
    :type file: :class:`File`
    
    :param date: Point in time (Unix timestamp) when the file was uploaded
    :type date: :class:`int`
    
    """

    ID: str = Field("datedFile", alias="@type")
    file: File
    date: int

    @staticmethod
    def read(q: dict) -> DatedFile:
        return DatedFile.construct(**q)
