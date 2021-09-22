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
    
    :param text: Cell text; may be null. If the text is null, then the cell should be invisible, defaults to None
    :type text: :class:`RichText`, optional
    
    :param is_header: True, if it is a header cell
    :type is_header: :class:`bool`
    
    :param colspan: The number of columns the cell should span
    :type colspan: :class:`int`
    
    :param rowspan: The number of rows the cell should span
    :type rowspan: :class:`int`
    
    :param align: Horizontal cell content alignment
    :type align: :class:`PageBlockHorizontalAlignment`
    
    :param valign: Vertical cell content alignment
    :type valign: :class:`PageBlockVerticalAlignment`
    
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
