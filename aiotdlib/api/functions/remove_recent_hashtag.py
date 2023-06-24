# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveRecentHashtag(BaseObject):
    """
    Removes a hashtag from the list of recently used hashtags

    :param hashtag: Hashtag to delete
    :type hashtag: :class:`String`
    """

    ID: typing.Literal["removeRecentHashtag"] = "removeRecentHashtag"
    hashtag: String
