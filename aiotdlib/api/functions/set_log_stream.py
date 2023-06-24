# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    LogStream,
)


class SetLogStream(BaseObject):
    """
    Sets new log stream for internal logging of TDLib. Can be called synchronously

    :param log_stream: New log stream
    :type log_stream: :class:`LogStream`
    """

    ID: typing.Literal["setLogStream"] = "setLogStream"
    log_stream: LogStream
