# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSuggestedFileName(BaseObject):
    """
    Returns suggested name for saving a file in a given directory

    :param file_id: Identifier of the file
    :type file_id: :class:`Int32`
    :param directory: Directory in which the file is supposed to be saved
    :type directory: :class:`String`
    """

    ID: typing.Literal["getSuggestedFileName"] = "getSuggestedFileName"
    file_id: Int32
    directory: String
