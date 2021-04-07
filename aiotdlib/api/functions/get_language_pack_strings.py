# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetLanguagePackStrings(BaseObject):
    """
    Returns strings from a language pack in the current localization target by their keys. Can be called before authorization
    
    Params:
        language_pack_id (:class:`str`)
            Language pack identifier of the strings to be returned
        
        keys (:obj:`list[str]`)
            Language pack keys of the strings to be returned; leave empty to request all available strings
        
    """

    ID: str = Field("getLanguagePackStrings", alias="@type")
    language_pack_id: str
    keys: list[str]

    @staticmethod
    def read(q: dict) -> GetLanguagePackStrings:
        return GetLanguagePackStrings.construct(**q)
