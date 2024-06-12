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
    Preliminary uploads a file to the cloud before sending it in a message, which can be useful for uploading of being recorded voice and video notes. In all other cases there is no need to preliminary upload a file. Updates updateFile will be used to notify about upload progress. The upload will not be completed until the file is sent in a message

    :param file: File to upload
    :type file: :class:`InputFile`
    :param priority: Priority of the upload (1-32). The higher the priority, the earlier the file will be uploaded. If the priorities of two files are equal, then the first one for which preliminaryUploadFile was called will be uploaded first
    :type priority: :class:`Int32`
    :param file_type: File type; pass null if unknown, defaults to None
    :type file_type: :class:`FileType`, optional
    """

    ID: typing.Literal["preliminaryUploadFile"] = Field(
        "preliminaryUploadFile", validation_alias="@type", alias="@type"
    )
    file: InputFile
    priority: Int32
    file_type: typing.Optional[FileType] = None
