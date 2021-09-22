# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class EncryptedCredentials(BaseObject):
    """
    Contains encrypted Telegram Passport data credentials
    
    :param data: The encrypted credentials
    :type data: :class:`str`
    
    :param hash_: The decrypted data hash
    :type hash_: :class:`str`
    
    :param secret: Secret for data decryption, encrypted with the service's public key
    :type secret: :class:`str`
    
    """

    ID: str = Field("encryptedCredentials", alias="@type")
    data: str
    hash_: str = Field(..., alias='hash')
    secret: str

    @staticmethod
    def read(q: dict) -> EncryptedCredentials:
        return EncryptedCredentials.construct(**q)
