# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetStickerSetTitle(BaseObject):
    """
    Sets a sticker set title; for bots only

    :param name: Sticker set name
    :type name: :class:`String`
    :param title: New sticker set title
    :type title: :class:`String`
    """

    ID: typing.Literal["setStickerSetTitle"] = "setStickerSetTitle"
    name: String
    title: String
