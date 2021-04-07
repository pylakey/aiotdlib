# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CancelDownloadFile(BaseObject):
    """
    Stops the downloading of a file. If a file has already been downloaded, does nothing
    
    Params:
        file_id (:class:`int`)
            Identifier of a file to stop downloading
        
        only_if_pending (:class:`bool`)
            Pass true to stop downloading only if it hasn't been started, i.e. request hasn't been sent to server
        
    """

    ID: str = Field("cancelDownloadFile", alias="@type")
    file_id: int
    only_if_pending: bool

    @staticmethod
    def read(q: dict) -> CancelDownloadFile:
        return CancelDownloadFile.construct(**q)
