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
    
    :param number: Document number; 1-24 characters
    :type number: :class:`str`
    
    :param expiry_date: Document expiry date; may be null, defaults to None
    :type expiry_date: :class:`Date`, optional
    
    :param front_side: Front side of the document
    :type front_side: :class:`DatedFile`
    
    :param reverse_side: Reverse side of the document; only for driver license and identity card; may be null, defaults to None
    :type reverse_side: :class:`DatedFile`, optional
    
    :param selfie: Selfie with the document; may be null, defaults to None
    :type selfie: :class:`DatedFile`, optional
    
    :param translation: List of files containing a certified English translation of the document
    :type translation: :class:`list[DatedFile]`
    
    """

    ID: str = Field("identityDocument", alias="@type")
    number: str = Field(..., min_length=1, max_length=24)
    expiry_date: typing.Optional[Date] = None
    front_side: DatedFile
    reverse_side: typing.Optional[DatedFile] = None
    selfie: typing.Optional[DatedFile] = None
    translation: list[DatedFile]

    @staticmethod
    def read(q: dict) -> IdentityDocument:
        return IdentityDocument.construct(**q)
