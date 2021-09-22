# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .date import Date
from .input_file import InputFile
from ..base_object import BaseObject


class InputIdentityDocument(BaseObject):
    """
    An identity document to be saved to Telegram Passport
    
    :param number: Document number; 1-24 characters
    :type number: :class:`str`
    
    :param expiry_date: Document expiry date, if available
    :type expiry_date: :class:`Date`
    
    :param front_side: Front side of the document
    :type front_side: :class:`InputFile`
    
    :param reverse_side: Reverse side of the document; only for driver license and identity card
    :type reverse_side: :class:`InputFile`
    
    :param selfie: Selfie with the document, if available
    :type selfie: :class:`InputFile`
    
    :param translation: List of files containing a certified English translation of the document
    :type translation: :class:`list[InputFile]`
    
    """

    ID: str = Field("inputIdentityDocument", alias="@type")
    number: str = Field(..., min_length=1, max_length=24)
    expiry_date: Date
    front_side: InputFile
    reverse_side: InputFile
    selfie: InputFile
    translation: list[InputFile]

    @staticmethod
    def read(q: dict) -> InputIdentityDocument:
        return InputIdentityDocument.construct(**q)
