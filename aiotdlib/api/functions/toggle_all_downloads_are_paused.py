# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleAllDownloadsArePaused(BaseObject):
    """
    Changes pause state of all files in the file download list

    :param are_paused: Pass true to pause all downloads; pass false to unpause them
    :type are_paused: :class:`Bool`
    """

    ID: typing.Literal["toggleAllDownloadsArePaused"] = "toggleAllDownloadsArePaused"
    are_paused: Bool = False
