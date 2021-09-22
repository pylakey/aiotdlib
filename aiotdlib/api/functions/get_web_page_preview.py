# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import FormattedText
from ..base_object import BaseObject


class GetWebPagePreview(BaseObject):
    """
    Returns a web page preview by the text of the message. Do not call this function too often. Returns a 404 error if the web page has no preview
    
    :param text: Message text with formatting
    :type text: :class:`FormattedText`
    
    """

    ID: str = Field("getWebPagePreview", alias="@type")
    text: FormattedText

    @staticmethod
    def read(q: dict) -> GetWebPagePreview:
        return GetWebPagePreview.construct(**q)
