# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetCloseFriends(BaseObject):
    """
    Changes the list of close friends of the current user

    :param user_ids: User identifiers of close friends; the users must be contacts of the current user
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["setCloseFriends"] = "setCloseFriends"
    user_ids: Vector[Int53]
