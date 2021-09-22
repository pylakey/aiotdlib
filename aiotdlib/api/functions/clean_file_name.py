# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CleanFileName(BaseObject):
    """
    Removes potentially dangerous characters from the name of a file. The encoding of the file name is supposed to be UTF-8. Returns an empty string on failure. Can be called synchronously
    
    :param file_name: File name or path to the file
    :type file_name: :class:`str`
    
    """

    ID: str = Field("cleanFileName", alias="@type")
    file_name: str

    @staticmethod
    def read(q: dict) -> CleanFileName:
        return CleanFileName.construct(**q)
