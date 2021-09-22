# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import LogStream
from ..base_object import BaseObject


class SetLogStream(BaseObject):
    """
    Sets new log stream for internal logging of TDLib. Can be called synchronously
    
    :param log_stream: New log stream
    :type log_stream: :class:`LogStream`
    
    """

    ID: str = Field("setLogStream", alias="@type")
    log_stream: LogStream

    @staticmethod
    def read(q: dict) -> SetLogStream:
        return SetLogStream.construct(**q)
