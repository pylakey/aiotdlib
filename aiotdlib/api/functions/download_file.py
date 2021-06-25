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
    
    Params:
        file_id (:class:`int`)
            Identifier of the file to download
        
        priority (:class:`int`)
            Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile was called will be downloaded first
        
        offset (:class:`int`)
            The starting position from which the file should be downloaded
        
        limit (:class:`int`)
            Number of bytes which should be downloaded starting from the "offset" position before the download will be automatically canceled; use 0 to download without a limit
        
        synchronous (:class:`bool`)
            If false, this request returns file state just after the download has been started. If true, this request returns file state only after the download has succeeded, has failed, has been canceled or a new downloadFile request with different offset/limit parameters was sent
        
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
