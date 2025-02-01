# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetExternalLinkInfo(BaseObject):
    """
    Returns information about an action to be done when the current user clicks an external link. Don't use this method for links from secret chats if link preview is disabled in secret chats

    :param link: The link
    :type link: :class:`String`
    """

    ID: typing.Literal["getExternalLinkInfo"] = Field("getExternalLinkInfo", validation_alias="@type", alias="@type")
    link: String
