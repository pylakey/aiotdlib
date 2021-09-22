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


class GetMarkdownText(BaseObject):
    """
    Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. Can be called synchronously
    
    :param text: The text
    :type text: :class:`FormattedText`
    
    """

    ID: str = Field("getMarkdownText", alias="@type")
    text: FormattedText

    @staticmethod
    def read(q: dict) -> GetMarkdownText:
        return GetMarkdownText.construct(**q)
