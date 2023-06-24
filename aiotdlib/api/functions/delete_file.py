# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteFile(BaseObject):
    """
    Deletes a file from the TDLib file cache

    :param file_id: Identifier of the file to delete
    :type file_id: :class:`Int32`
    """

    ID: typing.Literal["deleteFile"] = "deleteFile"
    file_id: Int32
