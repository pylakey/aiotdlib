# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessageFileType(BaseObject):
    """
    Returns information about a file with messages exported from another application

    :param message_file_head: Beginning of the message file; up to 100 first lines
    :type message_file_head: :class:`String`
    """

    ID: typing.Literal["getMessageFileType"] = "getMessageFileType"
    message_file_head: String
