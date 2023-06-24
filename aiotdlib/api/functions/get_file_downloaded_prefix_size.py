# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetFileDownloadedPrefixSize(BaseObject):
    """
    Returns file downloaded prefix size from a given offset, in bytes

    :param file_id: Identifier of the file
    :type file_id: :class:`Int32`
    :param offset: Offset from which downloaded prefix size needs to be calculated
    :type offset: :class:`Int53`
    """

    ID: typing.Literal["getFileDownloadedPrefixSize"] = "getFileDownloadedPrefixSize"
    file_id: Int32
    offset: Int53
