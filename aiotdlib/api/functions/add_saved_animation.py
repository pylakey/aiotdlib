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


class AddSavedAnimation(BaseObject):
    """
    Manually adds a new animation to the list of saved animations. The new animation is added to the beginning of the list. If the animation was already in the list, it is removed first. Only non-secret video animations with MIME type "video/mp4" can be added to the list

    :param animation: The animation file to be added. Only animations known to the server (i.e., successfully sent via a message) can be added to the list
    :type animation: :class:`InputFile`
    """

    ID: typing.Literal["addSavedAnimation"] = "addSavedAnimation"
    animation: InputFile
