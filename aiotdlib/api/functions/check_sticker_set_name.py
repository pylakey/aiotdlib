# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckStickerSetName(BaseObject):
    """
    Checks whether a name can be used for a new sticker set

    :param name: Name to be checked
    :type name: :class:`String`
    """

    ID: typing.Literal["checkStickerSetName"] = "checkStickerSetName"
    name: String
