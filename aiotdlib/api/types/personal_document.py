# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .dated_file import DatedFile
from ..base_object import BaseObject


class PersonalDocument(BaseObject):
    """
    A personal document, containing some information about a user
    
    Params:
        files (:obj:`list[DatedFile]`)
            List of files containing the pages of the document
        
        translation (:obj:`list[DatedFile]`)
            List of files containing a certified English translation of the document
        
    """

    ID: str = Field("personalDocument", alias="@type")
    files: list[DatedFile]
    translation: list[DatedFile]

    @staticmethod
    def read(q: dict) -> PersonalDocument:
        return PersonalDocument.construct(**q)
