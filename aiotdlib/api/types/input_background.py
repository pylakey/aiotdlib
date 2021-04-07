# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .input_file import InputFile
from ..base_object import BaseObject


class InputBackground(BaseObject):
    """
    Contains information about background to set
    
    """

    ID: str = Field("inputBackground", alias="@type")


class InputBackgroundLocal(InputBackground):
    """
    A background from a local file
    
    Params:
        background (:class:`InputFile`)
            Background file to use. Only inputFileLocal and inputFileGenerated are supported. The file must be in JPEG format for wallpapers and in PNG format for patterns
        
    """

    ID: str = Field("inputBackgroundLocal", alias="@type")
    background: InputFile

    @staticmethod
    def read(q: dict) -> InputBackgroundLocal:
        return InputBackgroundLocal.construct(**q)


class InputBackgroundRemote(InputBackground):
    """
    A background from the server
    
    Params:
        background_id (:class:`int`)
            The background identifier
        
    """

    ID: str = Field("inputBackgroundRemote", alias="@type")
    background_id: int

    @staticmethod
    def read(q: dict) -> InputBackgroundRemote:
        return InputBackgroundRemote.construct(**q)
