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
    InternalLinkType,
)


class GetInternalLink(BaseObject):
    """
    Returns an HTTPS or a tg: link with the given type. Can be called before authorization

    :param type_: Expected type of the link
    :type type_: :class:`InternalLinkType`
    :param is_http: Pass true to create an HTTPS link (only available for some link types); pass false to create a tg: link
    :type is_http: :class:`Bool`
    """

    ID: typing.Literal["getInternalLink"] = "getInternalLink"
    type_: InternalLinkType = Field(..., alias="type")
    is_http: Bool = False
