# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetApplicationDownloadLink(BaseObject):
    """
    Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram
    """

    ID: typing.Literal["getApplicationDownloadLink"] = "getApplicationDownloadLink"
