# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CancelDownloadFile(BaseObject):
    """
    Stops the downloading of a file. If a file has already been downloaded, does nothing
    
    :param file_id: Identifier of a file to stop downloading
    :type file_id: :class:`int`
    
    :param only_if_pending: Pass true to stop downloading only if it hasn't been started, i.e. request hasn't been sent to server
    :type only_if_pending: :class:`bool`
    
    """

    ID: str = Field("cancelDownloadFile", alias="@type")
    file_id: int
    only_if_pending: bool

    @staticmethod
    def read(q: dict) -> CancelDownloadFile:
        return CancelDownloadFile.construct(**q)
