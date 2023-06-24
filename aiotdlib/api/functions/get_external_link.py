# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetExternalLink(BaseObject):
    """
    Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed

    :param link: The HTTP link
    :type link: :class:`String`
    :param allow_write_access: Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages
    :type allow_write_access: :class:`Bool`
    """

    ID: typing.Literal["getExternalLink"] = "getExternalLink"
    link: String
    allow_write_access: Bool = False
