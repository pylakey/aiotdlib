# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .rich_text import RichText
from ..base_object import BaseObject


class PageBlockCaption(BaseObject):
    """
    Contains a caption of an instant view web page block, consisting of a text and a trailing credit
    
    :param text: Content of the caption
    :type text: :class:`RichText`
    
    :param credit: Block credit (like HTML tag <cite>)
    :type credit: :class:`RichText`
    
    """

    ID: str = Field("pageBlockCaption", alias="@type")
    text: RichText
    credit: RichText

    @staticmethod
    def read(q: dict) -> PageBlockCaption:
        return PageBlockCaption.construct(**q)
