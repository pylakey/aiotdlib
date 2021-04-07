# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import LanguagePackInfo


class EditCustomLanguagePackInfo(BaseObject):
    """
    Edits information about a custom local language pack in the current localization target. Can be called before authorization
    
    Params:
        info (:class:`LanguagePackInfo`)
            New information about the custom local language pack
        
    """

    ID: str = Field("editCustomLanguagePackInfo", alias="@type")
    info: LanguagePackInfo

    @staticmethod
    def read(q: dict) -> EditCustomLanguagePackInfo:
        return EditCustomLanguagePackInfo.construct(**q)
