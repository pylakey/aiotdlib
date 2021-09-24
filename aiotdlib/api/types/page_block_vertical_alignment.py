# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PageBlockVerticalAlignment(BaseObject):
    """
    Describes a Vertical alignment of a table cell content
    
    """

    ID: str = Field("pageBlockVerticalAlignment", alias="@type")


class PageBlockVerticalAlignmentBottom(PageBlockVerticalAlignment):
    """
    The content should be bottom-aligned
    
    """

    ID: str = Field("pageBlockVerticalAlignmentBottom", alias="@type")

    @staticmethod
    def read(q: dict) -> PageBlockVerticalAlignmentBottom:
        return PageBlockVerticalAlignmentBottom.construct(**q)


class PageBlockVerticalAlignmentMiddle(PageBlockVerticalAlignment):
    """
    The content should be middle-aligned
    
    """

    ID: str = Field("pageBlockVerticalAlignmentMiddle", alias="@type")

    @staticmethod
    def read(q: dict) -> PageBlockVerticalAlignmentMiddle:
        return PageBlockVerticalAlignmentMiddle.construct(**q)


class PageBlockVerticalAlignmentTop(PageBlockVerticalAlignment):
    """
    The content should be top-aligned
    
    """

    ID: str = Field("pageBlockVerticalAlignmentTop", alias="@type")

    @staticmethod
    def read(q: dict) -> PageBlockVerticalAlignmentTop:
        return PageBlockVerticalAlignmentTop.construct(**q)
