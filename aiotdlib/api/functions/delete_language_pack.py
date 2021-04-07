# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteLanguagePack(BaseObject):
    """
    Deletes all information about a language pack in the current localization target. The language pack which is currently in use (including base language pack) or is being synchronized can't be deleted. Can be called before authorization
    
    Params:
        language_pack_id (:class:`str`)
            Identifier of the language pack to delete
        
    """

    ID: str = Field("deleteLanguagePack", alias="@type")
    language_pack_id: str

    @staticmethod
    def read(q: dict) -> DeleteLanguagePack:
        return DeleteLanguagePack.construct(**q)
