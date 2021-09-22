# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .internal_link_type import InternalLinkType
from .page_block import PageBlock
from ..base_object import BaseObject


class WebPageInstantView(BaseObject):
    """
    Describes an instant view page for a web page
    
    :param page_blocks: Content of the web page
    :type page_blocks: :class:`list[PageBlock]`
    
    :param view_count: Number of the instant view views; 0 if unknown
    :type view_count: :class:`int`
    
    :param version: Version of the instant view, currently can be 1 or 2
    :type version: :class:`int`
    
    :param is_rtl: True, if the instant view must be shown from right to left
    :type is_rtl: :class:`bool`
    
    :param is_full: True, if the instant view contains the full page. A network request might be needed to get the full web page instant view
    :type is_full: :class:`bool`
    
    :param feedback_link: An internal link to be opened to leave feedback about the instant view
    :type feedback_link: :class:`InternalLinkType`
    
    """

    ID: str = Field("webPageInstantView", alias="@type")
    page_blocks: list[PageBlock]
    view_count: int
    version: int
    is_rtl: bool
    is_full: bool
    feedback_link: InternalLinkType

    @staticmethod
    def read(q: dict) -> WebPageInstantView:
        return WebPageInstantView.construct(**q)
