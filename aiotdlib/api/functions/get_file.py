# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetFile(BaseObject):
    """
    Returns information about a file. This is an offline method

    :param file_id: Identifier of the file to get
    :type file_id: :class:`Int32`
    """

    ID: typing.Literal["getFile"] = Field("getFile", validation_alias="@type", alias="@type")
    file_id: Int32
