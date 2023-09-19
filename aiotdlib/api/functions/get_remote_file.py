# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    FileType,
)


class GetRemoteFile(BaseObject):
    """
    Returns information about a file by its remote identifier; this is an offline request. Can be used to register a URL as a file for further uploading, or sending as a message. Even the request succeeds, the file can be used only if it is still accessible to the user. For example, if the file is from a message, then the message must be not deleted and accessible to the user. If the file database is disabled, then the corresponding object with the file must be preloaded by the application

    :param remote_file_id: Remote identifier of the file to get
    :type remote_file_id: :class:`String`
    :param file_type: File type; pass null if unknown, defaults to None
    :type file_type: :class:`FileType`, optional
    """

    ID: typing.Literal["getRemoteFile"] = "getRemoteFile"
    remote_file_id: String
    file_type: typing.Optional[FileType] = None
