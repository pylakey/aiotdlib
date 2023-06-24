# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReadFilePart(BaseObject):
    """
    Reads a part of a file from the TDLib file cache and returns read bytes. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct read from the file

    :param file_id: Identifier of the file. The file must be located in the TDLib file cache
    :type file_id: :class:`Int32`
    :param offset: The offset from which to read the file
    :type offset: :class:`Int53`
    :param count: Number of bytes to read. An error will be returned if there are not enough bytes available in the file from the specified position. Pass 0 to read all available data from the specified position
    :type count: :class:`Int53`
    """

    ID: typing.Literal["readFilePart"] = "readFilePart"
    file_id: Int32
    offset: Int53
    count: Int53
