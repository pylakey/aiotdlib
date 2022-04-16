# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DownloadFile(BaseObject):
    """
    Downloads a file from the cloud. Download progress and completion of the download will be notified through updateFile updates
    
    :param file_id: Identifier of the file to download
    :type file_id: :class:`int`
    
    :param priority: Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first
    :type priority: :class:`int`
    
    :param offset: The starting position from which the file needs to be downloaded
    :type offset: :class:`int`
    
    :param limit: Number of bytes which need to be downloaded starting from the "offset" position before the download will automatically be canceled; use 0 to download without a limit
    :type limit: :class:`int`
    
    :param synchronous: Pass true to return response only after the file download has succeeded, has failed, has been canceled, or a new downloadFile request with different offset/limit parameters was sent; pass false to return file state immediately, just after the download has been started
    :type synchronous: :class:`bool`
    
    """

    ID: str = Field("downloadFile", alias="@type")
    file_id: int
    priority: int
    offset: int
    limit: int
    synchronous: bool

    @staticmethod
    def read(q: dict) -> DownloadFile:
        return DownloadFile.construct(**q)
