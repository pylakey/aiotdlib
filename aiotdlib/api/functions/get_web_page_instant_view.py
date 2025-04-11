# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetWebPageInstantView(BaseObject):
    """
    Returns an instant view version of a web page if available. This is an offline method if only_local is true. Returns a 404 error if the web page has no instant view page

    :param url: The web page URL
    :type url: :class:`String`
    :param only_local: Pass true to get only locally available information without sending network requests
    :type only_local: :class:`Bool`
    """

    ID: typing.Literal["getWebPageInstantView"] = Field(
        "getWebPageInstantView", validation_alias="@type", alias="@type"
    )
    url: String
    only_local: Bool = False
