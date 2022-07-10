# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AddFileToDownloads(BaseObject):
    """
    Adds a file from a message to the list of file downloads. Download progress and completion of the download will be notified through updateFile updates. If message database is used, the list of file downloads is persistent across application restarts. The downloading is independent from download using downloadFile, i.e. it continues if downloadFile is canceled or is used to download a part of the file
    
    :param file_id: Identifier of the file to download
    :type file_id: :class:`int`
    
    :param chat_id: Chat identifier of the message with the file
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param priority: Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first
    :type priority: :class:`int`
    
    """

    ID: str = Field("addFileToDownloads", alias="@type")
    file_id: int
    chat_id: int
    message_id: int
    priority: int

    @staticmethod
    def read(q: dict) -> AddFileToDownloads:
        return AddFileToDownloads.construct(**q)
