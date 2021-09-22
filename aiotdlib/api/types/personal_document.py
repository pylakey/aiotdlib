# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .dated_file import DatedFile
from ..base_object import BaseObject


class PersonalDocument(BaseObject):
    """
    A personal document, containing some information about a user
    
    :param files: List of files containing the pages of the document
    :type files: :class:`list[DatedFile]`
    
    :param translation: List of files containing a certified English translation of the document
    :type translation: :class:`list[DatedFile]`
    
    """

    ID: str = Field("personalDocument", alias="@type")
    files: list[DatedFile]
    translation: list[DatedFile]

    @staticmethod
    def read(q: dict) -> PersonalDocument:
        return PersonalDocument.construct(**q)
