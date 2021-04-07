# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import OptionValue


class SetOption(BaseObject):
    """
    Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization
    
    Params:
        name (:class:`str`)
            The name of the option
        
        value (:class:`OptionValue`)
            The new value of the option
        
    """

    ID: str = Field("setOption", alias="@type")
    name: str
    value: OptionValue

    @staticmethod
    def read(q: dict) -> SetOption:
        return SetOption.construct(**q)
