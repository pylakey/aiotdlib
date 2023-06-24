# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    FormattedText,
)


class GetMarkdownText(BaseObject):
    """
    Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. Can be called synchronously

    :param text: The text
    :type text: :class:`FormattedText`
    """

    ID: typing.Literal["getMarkdownText"] = "getMarkdownText"
    text: FormattedText
