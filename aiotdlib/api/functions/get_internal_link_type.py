# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetInternalLinkType(BaseObject):
    """
    Returns information about the type of internal link. Returns a 404 error if the link is not internal. Can be called before authorization

    :param link: The link
    :type link: :class:`String`
    """

    ID: typing.Literal["getInternalLinkType"] = Field("getInternalLinkType", validation_alias="@type", alias="@type")
    link: String
