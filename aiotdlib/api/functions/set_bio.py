# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetBio(BaseObject):
    """
    Changes the bio of the current user

    :param bio: The new value of the user bio; 0-getOption("bio_length_max") characters without line feeds
    :type bio: :class:`String`
    """

    ID: typing.Literal["setBio"] = "setBio"
    bio: String
