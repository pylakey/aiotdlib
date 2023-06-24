# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleDownloadIsPaused(BaseObject):
    """
    Changes pause state of a file in the file download list

    :param file_id: Identifier of the downloaded file
    :type file_id: :class:`Int32`
    :param is_paused: Pass true if the download is paused
    :type is_paused: :class:`Bool`
    """

    ID: typing.Literal["toggleDownloadIsPaused"] = "toggleDownloadIsPaused"
    file_id: Int32
    is_paused: Bool = False
