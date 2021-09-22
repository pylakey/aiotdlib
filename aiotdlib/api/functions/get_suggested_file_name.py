# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetSuggestedFileName(BaseObject):
    """
    Returns suggested name for saving a file in a given directory
    
    :param file_id: Identifier of the file
    :type file_id: :class:`int`
    
    :param directory: Directory in which the file is supposed to be saved
    :type directory: :class:`str`
    
    """

    ID: str = Field("getSuggestedFileName", alias="@type")
    file_id: int
    directory: str

    @staticmethod
    def read(q: dict) -> GetSuggestedFileName:
        return GetSuggestedFileName.construct(**q)
