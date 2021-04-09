# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .page_block_horizontal_alignment import PageBlockHorizontalAlignment
from .page_block_vertical_alignment import PageBlockVerticalAlignment
from .rich_text import RichText
from ..base_object import BaseObject


class PageBlockTableCell(BaseObject):
    """
    Represents a cell of a table
    
    Params:
        text (:class:`RichText`)
            Cell text; may be null. If the text is null, then the cell should be invisible
        
        is_header (:class:`bool`)
            True, if it is a header cell
        
        colspan (:class:`int`)
            The number of columns the cell should span
        
        rowspan (:class:`int`)
            The number of rows the cell should span
        
        align (:class:`PageBlockHorizontalAlignment`)
            Horizontal cell content alignment
        
        valign (:class:`PageBlockVerticalAlignment`)
            Vertical cell content alignment
        
    """

    ID: str = Field("pageBlockTableCell", alias="@type")
    text: typing.Optional[RichText] = None
    is_header: bool
    colspan: int
    rowspan: int
    align: PageBlockHorizontalAlignment
    valign: PageBlockVerticalAlignment

    @staticmethod
    def read(q: dict) -> PageBlockTableCell:
        return PageBlockTableCell.construct(**q)
