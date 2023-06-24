# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetRecentlyVisitedTMeUrls(BaseObject):
    """
    Returns t.me URLs recently visited by a newly registered user

    :param referrer: Google Play referrer to identify the user
    :type referrer: :class:`String`
    """

    ID: typing.Literal["getRecentlyVisitedTMeUrls"] = "getRecentlyVisitedTMeUrls"
    referrer: String
