# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetFileExtension(BaseObject):
    """
    Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. Can be called synchronously

    :param mime_type: The MIME type of the file
    :type mime_type: :class:`String`
    """

    ID: typing.Literal["getFileExtension"] = "getFileExtension"
    mime_type: String
