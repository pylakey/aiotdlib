# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchBackground(BaseObject):
    """
    Searches for a background by its name

    :param name: The name of the background
    :type name: :class:`String`
    """

    ID: typing.Literal["searchBackground"] = "searchBackground"
    name: String
