# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AddCustomServerLanguagePack(BaseObject):
    """
    Adds a custom server language pack to the list of installed language packs in current localization target. Can be called before authorization
    
    Params:
        language_pack_id (:class:`str`)
            Identifier of a language pack to be added; may be different from a name that is used in an "https://t.me/setlanguage/" link
        
    """

    ID: str = Field("addCustomServerLanguagePack", alias="@type")
    language_pack_id: str

    @staticmethod
    def read(q: dict) -> AddCustomServerLanguagePack:
        return AddCustomServerLanguagePack.construct(**q)
