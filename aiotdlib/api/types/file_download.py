# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message import Message
from ..base_object import BaseObject


class FileDownload(BaseObject):
    """
    Describes a file added to file download list
    
    :param file_id: File identifier
    :type file_id: :class:`int`
    
    :param message: The message with the file
    :type message: :class:`Message`
    
    :param add_date: Point in time (Unix timestamp) when the file was added to the download list
    :type add_date: :class:`int`
    
    :param complete_date: Point in time (Unix timestamp) when the file downloading was completed; 0 if the file downloading isn't completed
    :type complete_date: :class:`int`
    
    :param is_paused: True, if downloading of the file is paused
    :type is_paused: :class:`bool`
    
    """

    ID: str = Field("fileDownload", alias="@type")
    file_id: int
    message: Message
    add_date: int
    complete_date: int
    is_paused: bool

    @staticmethod
    def read(q: dict) -> FileDownload:
        return FileDownload.construct(**q)
