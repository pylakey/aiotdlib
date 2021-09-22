# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import OptionValue
from ..base_object import BaseObject


class SetOption(BaseObject):
    """
    Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization
    
    :param name: The name of the option
    :type name: :class:`str`
    
    :param value: The new value of the option
    :type value: :class:`OptionValue`
    
    """

    ID: str = Field("setOption", alias="@type")
    name: str
    value: OptionValue

    @staticmethod
    def read(q: dict) -> SetOption:
        return SetOption.construct(**q)
