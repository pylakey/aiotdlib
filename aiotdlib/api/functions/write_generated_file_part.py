# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class WriteGeneratedFilePart(BaseObject):
    """
    Writes a part of a generated file. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file

    :param generation_id: The identifier of the generation process
    :type generation_id: :class:`Int64`
    :param offset: The offset from which to write the data to the file
    :type offset: :class:`Int53`
    :param data: The data to write
    :type data: :class:`Bytes`
    """

    ID: typing.Literal["writeGeneratedFilePart"] = "writeGeneratedFilePart"
    generation_id: Int64
    offset: Int53
    data: Bytes
