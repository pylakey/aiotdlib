# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class EncryptedCredentials(BaseObject):
    """
    Contains encrypted Telegram Passport data credentials
    
    Params:
        data (:class:`str`)
            The encrypted credentials
        
        hash_ (:class:`str`)
            The decrypted data hash
        
        secret (:class:`str`)
            Secret for data decryption, encrypted with the service's public key
        
    """

    ID: str = Field("encryptedCredentials", alias="@type")
    data: str
    hash_: str = Field(..., alias='hash')
    secret: str

    @staticmethod
    def read(q: dict) -> EncryptedCredentials:
        return EncryptedCredentials.construct(**q)
