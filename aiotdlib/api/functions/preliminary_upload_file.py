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
    InputFile,
)


class PreliminaryUploadFile(BaseObject):
    """
    Preliminary uploads a file to the cloud before sending it in a message, which can be useful for uploading of being recorded voice and video notes. Updates updateFile will be used to notify about upload progress and successful completion of the upload. The file will not have a persistent remote identifier until it will be sent in a message

    :param file: File to upload
    :type file: :class:`InputFile`
    :param priority: Priority of the upload (1-32). The higher the priority, the earlier the file will be uploaded. If the priorities of two files are equal, then the first one for which preliminaryUploadFile was called will be uploaded first
    :type priority: :class:`Int32`
    :param file_type: File type; pass null if unknown, defaults to None
    :type file_type: :class:`FileType`, optional
    """

    ID: typing.Literal["preliminaryUploadFile"] = "preliminaryUploadFile"
    file: InputFile
    priority: Int32
    file_type: typing.Optional[FileType] = None
