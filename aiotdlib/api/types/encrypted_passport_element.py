# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .dated_file import DatedFile
from .passport_element_type import PassportElementType
from ..base_object import BaseObject


class EncryptedPassportElement(BaseObject):
    """
    Contains information about an encrypted Telegram Passport element; for bots only
    
    Params:
        type_ (:class:`PassportElementType`)
            Type of Telegram Passport element
        
        data (:class:`str`)
            Encrypted JSON-encoded data about the user
        
        front_side (:class:`DatedFile`)
            The front side of an identity document
        
        reverse_side (:class:`DatedFile`)
            The reverse side of an identity document; may be null
        
        selfie (:class:`DatedFile`)
            Selfie with the document; may be null
        
        translation (:obj:`list[DatedFile]`)
            List of files containing a certified English translation of the document
        
        files (:obj:`list[DatedFile]`)
            List of attached files
        
        value (:class:`str`)
            Unencrypted data, phone number or email address
        
        hash_ (:class:`str`)
            Hash of the entire element
        
    """

    ID: str = Field("encryptedPassportElement", alias="@type")
    type_: PassportElementType = Field(..., alias='type')
    data: str
    front_side: DatedFile
    reverse_side: typing.Optional[DatedFile] = None
    selfie: typing.Optional[DatedFile] = None
    translation: list[DatedFile]
    files: list[DatedFile]
    value: str
    hash_: str = Field(..., alias='hash')

    @staticmethod
    def read(q: dict) -> EncryptedPassportElement:
        return EncryptedPassportElement.construct(**q)
