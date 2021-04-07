# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .rich_text import RichText
from ..base_object import BaseObject


class PageBlockCaption(BaseObject):
    """
    Contains a caption of an instant view web page block, consisting of a text and a trailing credit
    
    Params:
        text (:class:`RichText`)
            Content of the caption
        
        credit (:class:`RichText`)
            Block credit (like HTML tag <cite>)
        
    """

    ID: str = Field("pageBlockCaption", alias="@type")
    text: RichText
    credit: RichText

    @staticmethod
    def read(q: dict) -> PageBlockCaption:
        return PageBlockCaption.construct(**q)
