# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CancelDownloadFile(BaseObject):
    """
    Stops the downloading of a file. If a file has already been downloaded, does nothing

    :param file_id: Identifier of a file to stop downloading
    :type file_id: :class:`Int32`
    :param only_if_pending: Pass true to stop downloading only if it hasn't been started, i.e. request hasn't been sent to server
    :type only_if_pending: :class:`Bool`
    """

    ID: typing.Literal["cancelDownloadFile"] = "cancelDownloadFile"
    file_id: Int32
    only_if_pending: Bool = False
