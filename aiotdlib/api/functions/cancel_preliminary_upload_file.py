# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CancelPreliminaryUploadFile(BaseObject):
    """
    Stops the preliminary uploading of a file. Supported only for files uploaded by using preliminaryUploadFile

    :param file_id: Identifier of the file to stop uploading
    :type file_id: :class:`Int32`
    """

    ID: typing.Literal["cancelPreliminaryUploadFile"] = Field(
        "cancelPreliminaryUploadFile", validation_alias="@type", alias="@type"
    )
    file_id: Int32
