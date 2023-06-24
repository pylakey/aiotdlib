# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveBackground(BaseObject):
    """
    Removes background from the list of installed backgrounds

    :param background_id: The background identifier
    :type background_id: :class:`Int64`
    """

    ID: typing.Literal["removeBackground"] = "removeBackground"
    background_id: Int64
