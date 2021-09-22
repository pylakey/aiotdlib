# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import LanguagePackInfo
from ..base_object import BaseObject


class EditCustomLanguagePackInfo(BaseObject):
    """
    Edits information about a custom local language pack in the current localization target. Can be called before authorization
    
    :param info: New information about the custom local language pack
    :type info: :class:`LanguagePackInfo`
    
    """

    ID: str = Field("editCustomLanguagePackInfo", alias="@type")
    info: LanguagePackInfo

    @staticmethod
    def read(q: dict) -> EditCustomLanguagePackInfo:
        return EditCustomLanguagePackInfo.construct(**q)
