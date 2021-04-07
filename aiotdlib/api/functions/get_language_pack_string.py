# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetLanguagePackString(BaseObject):
    """
    Returns a string stored in the local database from the specified localization target and language pack by its key. Returns a 404 error if the string is not found. Can be called synchronously
    
    Params:
        language_pack_database_path (:class:`str`)
            Path to the language pack database in which strings are stored
        
        localization_target (:class:`str`)
            Localization target to which the language pack belongs
        
        language_pack_id (:class:`str`)
            Language pack identifier
        
        key (:class:`str`)
            Language pack key of the string to be returned
        
    """

    ID: str = Field("getLanguagePackString", alias="@type")
    language_pack_database_path: str
    localization_target: str
    language_pack_id: str
    key: str

    @staticmethod
    def read(q: dict) -> GetLanguagePackString:
        return GetLanguagePackString.construct(**q)
