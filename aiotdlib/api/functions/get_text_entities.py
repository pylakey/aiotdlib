# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetTextEntities(BaseObject):
    """
    Returns all entities (mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses) found in the text. Can be called synchronously

    :param text: The text in which to look for entities
    :type text: :class:`String`
    """

    ID: typing.Literal["getTextEntities"] = "getTextEntities"
    text: String
