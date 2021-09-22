# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import FileType
from ..base_object import BaseObject


class GetRemoteFile(BaseObject):
    """
    Returns information about a file by its remote ID; this is an offline request. Can be used to register a URL as a file for further uploading, or sending as a message. Even the request succeeds, the file can be used only if it is still accessible to the user. For example, if the file is from a message, then the message must be not deleted and accessible to the user. If the file database is disabled, then the corresponding object with the file must be preloaded by the application
    
    :param remote_file_id: Remote identifier of the file to get
    :type remote_file_id: :class:`str`
    
    :param file_type: File type, if known
    :type file_type: :class:`FileType`
    
    """

    ID: str = Field("getRemoteFile", alias="@type")
    remote_file_id: str
    file_type: FileType

    @staticmethod
    def read(q: dict) -> GetRemoteFile:
        return GetRemoteFile.construct(**q)
