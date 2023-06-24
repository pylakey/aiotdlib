# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DownloadFile(BaseObject):
    """
    Downloads a file from the cloud. Download progress and completion of the download will be notified through updateFile updates

    :param file_id: Identifier of the file to download
    :type file_id: :class:`Int32`
    :param priority: Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first
    :type priority: :class:`Int32`
    :param offset: The starting position from which the file needs to be downloaded
    :type offset: :class:`Int53`
    :param limit: Number of bytes which need to be downloaded starting from the "offset" position before the download will automatically be canceled; use 0 to download without a limit
    :type limit: :class:`Int53`
    :param synchronous: Pass true to return response only after the file download has succeeded, has failed, has been canceled, or a new downloadFile request with different offset/limit parameters was sent; pass false to return file state immediately, just after the download has been started
    :type synchronous: :class:`Bool`
    """

    ID: typing.Literal["downloadFile"] = "downloadFile"
    file_id: Int32
    priority: Int32
    offset: Int53
    limit: Int53
    synchronous: Bool = False
