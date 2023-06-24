# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetFileMimeType(BaseObject):
    """
    Returns the MIME type of a file, guessed by its extension. Returns an empty string on failure. Can be called synchronously

    :param file_name: The name of the file or path to the file
    :type file_name: :class:`String`
    """

    ID: typing.Literal["getFileMimeType"] = "getFileMimeType"
    file_name: String
