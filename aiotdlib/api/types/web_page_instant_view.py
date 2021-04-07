# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .page_block import PageBlock
from ..base_object import BaseObject


class WebPageInstantView(BaseObject):
    """
    Describes an instant view page for a web page
    
    Params:
        page_blocks (:obj:`list[PageBlock]`)
            Content of the web page
        
        view_count (:class:`int`)
            Number of the instant view views; 0 if unknown
        
        version (:class:`int`)
            Version of the instant view, currently can be 1 or 2
        
        is_rtl (:class:`bool`)
            True, if the instant view must be shown from right to left
        
        is_full (:class:`bool`)
            True, if the instant view contains the full page. A network request might be needed to get the full web page instant view
        
    """

    ID: str = Field("webPageInstantView", alias="@type")
    page_blocks: list[PageBlock]
    view_count: int
    version: int
    is_rtl: bool
    is_full: bool

    @staticmethod
    def read(q: dict) -> WebPageInstantView:
        return WebPageInstantView.construct(**q)
