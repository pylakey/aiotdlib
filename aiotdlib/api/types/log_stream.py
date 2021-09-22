# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class LogStream(BaseObject):
    """
    Describes a stream to which TDLib internal log is written
    
    """

    ID: str = Field("logStream", alias="@type")


class LogStreamDefault(LogStream):
    """
    The log is written to stderr or an OS specific log
    
    """

    ID: str = Field("logStreamDefault", alias="@type")

    @staticmethod
    def read(q: dict) -> LogStreamDefault:
        return LogStreamDefault.construct(**q)


class LogStreamEmpty(LogStream):
    """
    The log is written nowhere
    
    """

    ID: str = Field("logStreamEmpty", alias="@type")

    @staticmethod
    def read(q: dict) -> LogStreamEmpty:
        return LogStreamEmpty.construct(**q)


class LogStreamFile(LogStream):
    """
    The log is written to a file
    
    :param path: Path to the file to where the internal TDLib log will be written
    :type path: :class:`str`
    
    :param max_file_size: The maximum size of the file to where the internal TDLib log is written before the file will be auto-rotated, in bytes
    :type max_file_size: :class:`int`
    
    :param redirect_stderr: Pass true to additionally redirect stderr to the log file. Ignored on Windows
    :type redirect_stderr: :class:`bool`
    
    """

    ID: str = Field("logStreamFile", alias="@type")
    path: str
    max_file_size: int
    redirect_stderr: bool

    @staticmethod
    def read(q: dict) -> LogStreamFile:
        return LogStreamFile.construct(**q)
