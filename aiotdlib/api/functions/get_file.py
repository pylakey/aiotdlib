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
    Returns information about a file; this is an offline request

    :param file_id: Identifier of the file to get
    :type file_id: :class:`Int32`
    """

    ID: typing.Literal["getFile"] = "getFile"
    file_id: Int32
