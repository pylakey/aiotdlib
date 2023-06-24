# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetUserLink(BaseObject):
    """
    Returns an HTTPS link, which can be used to get information about the current user
    """

    ID: typing.Literal["getUserLink"] = "getUserLink"
