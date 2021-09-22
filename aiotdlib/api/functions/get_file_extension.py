# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetFileExtension(BaseObject):
    """
    Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. Can be called synchronously
    
    :param mime_type: The MIME type of the file
    :type mime_type: :class:`str`
    
    """

    ID: str = Field("getFileExtension", alias="@type")
    mime_type: str

    @staticmethod
    def read(q: dict) -> GetFileExtension:
        return GetFileExtension.construct(**q)
