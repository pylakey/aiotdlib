# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .date import Date
from .dated_file import DatedFile
from ..base_object import BaseObject


class IdentityDocument(BaseObject):
    """
    An identity document
    
    Params:
        number (:class:`str`)
            Document number; 1-24 characters
        
        expiry_date (:class:`Date`)
            Document expiry date; may be null
        
        front_side (:class:`DatedFile`)
            Front side of the document
        
        reverse_side (:class:`DatedFile`)
            Reverse side of the document; only for driver license and identity card
        
        selfie (:class:`DatedFile`)
            Selfie with the document; may be null
        
        translation (:obj:`list[DatedFile]`)
            List of files containing a certified English translation of the document
        
    """

    ID: str = Field("identityDocument", alias="@type")
    number: str = Field(..., min_length=1, max_length=24)
    expiry_date: typing.Optional[Date] = None
    front_side: DatedFile
    reverse_side: DatedFile
    selfie: typing.Optional[DatedFile] = None
    translation: list[DatedFile]

    @staticmethod
    def read(q: dict) -> IdentityDocument:
        return IdentityDocument.construct(**q)
