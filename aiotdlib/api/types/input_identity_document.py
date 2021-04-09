# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .date import Date
from .input_file import InputFile
from ..base_object import BaseObject


class InputIdentityDocument(BaseObject):
    """
    An identity document to be saved to Telegram Passport
    
    Params:
        number (:class:`str`)
            Document number; 1-24 characters
        
        expiry_date (:class:`Date`)
            Document expiry date, if available
        
        front_side (:class:`InputFile`)
            Front side of the document
        
        reverse_side (:class:`InputFile`)
            Reverse side of the document; only for driver license and identity card
        
        selfie (:class:`InputFile`)
            Selfie with the document, if available
        
        translation (:obj:`list[InputFile]`)
            List of files containing a certified English translation of the document
        
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
