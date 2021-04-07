# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PageBlockHorizontalAlignment(BaseObject):
    """
    Describes a horizontal alignment of a table cell content
    
    """

    ID: str = Field("pageBlockHorizontalAlignment", alias="@type")


class PageBlockHorizontalAlignmentCenter(PageBlockHorizontalAlignment):
    """
    The content should be center-aligned
    
    """

    ID: str = Field("pageBlockHorizontalAlignmentCenter", alias="@type")

    @staticmethod
    def read(q: dict) -> PageBlockHorizontalAlignmentCenter:
        return PageBlockHorizontalAlignmentCenter.construct(**q)


class PageBlockHorizontalAlignmentLeft(PageBlockHorizontalAlignment):
    """
    The content should be left-aligned
    
    """

    ID: str = Field("pageBlockHorizontalAlignmentLeft", alias="@type")

    @staticmethod
    def read(q: dict) -> PageBlockHorizontalAlignmentLeft:
        return PageBlockHorizontalAlignmentLeft.construct(**q)


class PageBlockHorizontalAlignmentRight(PageBlockHorizontalAlignment):
    """
    The content should be right-aligned
    
    """

    ID: str = Field("pageBlockHorizontalAlignmentRight", alias="@type")

    @staticmethod
    def read(q: dict) -> PageBlockHorizontalAlignmentRight:
        return PageBlockHorizontalAlignmentRight.construct(**q)
