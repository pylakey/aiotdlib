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
    
    :param type_: Type of Telegram Passport element
    :type type_: :class:`PassportElementType`
    
    :param data: Encrypted JSON-encoded data about the user
    :type data: :class:`str`
    
    :param front_side: The front side of an identity document
    :type front_side: :class:`DatedFile`
    
    :param reverse_side: The reverse side of an identity document; may be null, defaults to None
    :type reverse_side: :class:`DatedFile`, optional
    
    :param selfie: Selfie with the document; may be null, defaults to None
    :type selfie: :class:`DatedFile`, optional
    
    :param translation: List of files containing a certified English translation of the document
    :type translation: :class:`list[DatedFile]`
    
    :param files: List of attached files
    :type files: :class:`list[DatedFile]`
    
    :param value: Unencrypted data, phone number or email address
    :type value: :class:`str`
    
    :param hash_: Hash of the entire element
    :type hash_: :class:`str`
    
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
