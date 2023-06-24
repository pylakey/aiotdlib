# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetUserProfilePhotos(BaseObject):
    """
    Returns the profile photos of a user. Personal and public photo aren't returned

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param offset: The number of photos to skip; must be non-negative
    :type offset: :class:`Int32`
    :param limit: The maximum number of photos to be returned; up to 100
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getUserProfilePhotos"] = "getUserProfilePhotos"
    user_id: Int53
    offset: Int32
    limit: Int32
