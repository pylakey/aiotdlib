# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetDatabaseEncryptionKey(BaseObject):
    """
    Changes the database encryption key. Usually the encryption key is never changed and is stored in some OS keychain
    
    Params:
        new_encryption_key (:class:`str`)
            New encryption key
        
    """

    ID: str = Field("setDatabaseEncryptionKey", alias="@type")
    new_encryption_key: str

    @staticmethod
    def read(q: dict) -> SetDatabaseEncryptionKey:
        return SetDatabaseEncryptionKey.construct(**q)
