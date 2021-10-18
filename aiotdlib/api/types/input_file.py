# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class InputFile(BaseObject):
    """
    Points to a file
    
    """

    ID: str = Field("inputFile", alias="@type")


class InputFileGenerated(InputFile):
    """
    A file generated by the application
    
    :param original_path: Local path to a file from which the file is generated; may be empty if there is no such file
    :type original_path: :class:`str`
    
    :param conversion: String specifying the conversion applied to the original file; must be persistent across application restarts. Conversions beginning with '#' are reserved for internal TDLib usage
    :type conversion: :class:`str`
    
    :param expected_size: Expected size of the generated file, in bytes; 0 if unknown
    :type expected_size: :class:`int`
    
    """

    ID: str = Field("inputFileGenerated", alias="@type")
    original_path: str
    conversion: str
    expected_size: int

    @staticmethod
    def read(q: dict) -> InputFileGenerated:
        return InputFileGenerated.construct(**q)


class InputFileId(InputFile):
    """
    A file defined by its unique ID
    
    :param id: Unique file identifier
    :type id: :class:`int`
    
    """

    ID: str = Field("inputFileId", alias="@type")
    id: int

    @staticmethod
    def read(q: dict) -> InputFileId:
        return InputFileId.construct(**q)


class InputFileLocal(InputFile):
    """
    A file defined by a local path
    
    :param path: Local path to the file
    :type path: :class:`str`
    
    """

    ID: str = Field("inputFileLocal", alias="@type")
    path: str

    @staticmethod
    def read(q: dict) -> InputFileLocal:
        return InputFileLocal.construct(**q)


class InputFileRemote(InputFile):
    """
    A file defined by its remote ID. The remote ID is guaranteed to be usable only if the corresponding file is still accessible to the user and known to TDLib. For example, if the file is from a message, then the message must be not deleted and accessible to the user. If the file database is disabled, then the corresponding object with the file must be preloaded by the application
    
    :param id: Remote file identifier
    :type id: :class:`str`
    
    """

    ID: str = Field("inputFileRemote", alias="@type")
    id: str

    @staticmethod
    def read(q: dict) -> InputFileRemote:
        return InputFileRemote.construct(**q)
