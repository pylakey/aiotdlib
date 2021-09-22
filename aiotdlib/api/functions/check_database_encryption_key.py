# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CheckDatabaseEncryptionKey(BaseObject):
    """
    Checks the database encryption key for correctness. Works only when the current authorization state is authorizationStateWaitEncryptionKey
    
    :param encryption_key: Encryption key to check or set up
    :type encryption_key: :class:`str`
    
    """

    ID: str = Field("checkDatabaseEncryptionKey", alias="@type")
    encryption_key: str

    @staticmethod
    def read(q: dict) -> CheckDatabaseEncryptionKey:
        return CheckDatabaseEncryptionKey.construct(**q)
