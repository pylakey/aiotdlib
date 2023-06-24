# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    InputFile,
)


class RemoveSavedAnimation(BaseObject):
    """
    Removes an animation from the list of saved animations

    :param animation: Animation file to be removed
    :type animation: :class:`InputFile`
    """

    ID: typing.Literal["removeSavedAnimation"] = "removeSavedAnimation"
    animation: InputFile
