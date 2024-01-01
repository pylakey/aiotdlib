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


class GetWebPagePreview(BaseObject):
    """
    Returns a web page preview by the text of the message. Do not call this function too often. Returns a 404 error if the web page has no preview

    :param text: Message text with formatting
    :type text: :class:`FormattedText`
    """

    ID: typing.Literal["getWebPagePreview"] = Field("getWebPagePreview", validation_alias="@type", alias="@type")
    text: FormattedText
