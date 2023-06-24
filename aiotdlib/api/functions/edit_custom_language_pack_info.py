# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    LanguagePackInfo,
)


class EditCustomLanguagePackInfo(BaseObject):
    """
    Edits information about a custom local language pack in the current localization target. Can be called before authorization

    :param info: New information about the custom local language pack
    :type info: :class:`LanguagePackInfo`
    """

    ID: typing.Literal["editCustomLanguagePackInfo"] = "editCustomLanguagePackInfo"
    info: LanguagePackInfo
