# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import FileType, InputFile


class UploadFile(BaseObject):
    """
    Asynchronously uploads a file to the cloud without sending it in a message. updateFile will be used to notify about upload progress and successful completion of the upload. The file will not have a persistent remote identifier until it will be sent in a message
    
    Params:
        file (:class:`InputFile`)
            File to upload
        
        file_type (:class:`FileType`)
            File type
        
        priority (:class:`int`)
            Priority of the upload (1-32). The higher the priority, the earlier the file will be uploaded. If the priorities of two files are equal, then the first one for which uploadFile was called will be uploaded first
        
    """

    ID: str = Field("uploadFile", alias="@type")
    file: InputFile
    file_type: FileType
    priority: int

    @staticmethod
    def read(q: dict) -> UploadFile:
        return UploadFile.construct(**q)
