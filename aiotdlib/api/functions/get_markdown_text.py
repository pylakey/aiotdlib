# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import FormattedText


class GetMarkdownText(BaseObject):
    """
    Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. Can be called synchronously
    
    Params:
        text (:class:`FormattedText`)
            The text
        
    """

    ID: str = Field("getMarkdownText", alias="@type")
    text: FormattedText

    @staticmethod
    def read(q: dict) -> GetMarkdownText:
        return GetMarkdownText.construct(**q)
