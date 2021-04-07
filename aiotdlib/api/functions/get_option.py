# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetOption(BaseObject):
    """
    Returns the value of an option by its name. (Check the list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization
    
    Params:
        name (:class:`str`)
            The name of the option
        
    """

    ID: str = Field("getOption", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> GetOption:
        return GetOption.construct(**q)
