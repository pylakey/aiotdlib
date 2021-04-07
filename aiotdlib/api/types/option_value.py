# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class OptionValue(BaseObject):
    """
    Represents the value of an option
    
    """

    ID: str = Field("optionValue", alias="@type")


class OptionValueBoolean(OptionValue):
    """
    Represents a boolean option
    
    Params:
        value (:class:`bool`)
            The value of the option
        
    """

    ID: str = Field("optionValueBoolean", alias="@type")
    value: bool

    @staticmethod
    def read(q: dict) -> OptionValueBoolean:
        return OptionValueBoolean.construct(**q)


class OptionValueEmpty(OptionValue):
    """
    Represents an unknown option or an option which has a default value
    
    """

    ID: str = Field("optionValueEmpty", alias="@type")

    @staticmethod
    def read(q: dict) -> OptionValueEmpty:
        return OptionValueEmpty.construct(**q)


class OptionValueInteger(OptionValue):
    """
    Represents an integer option
    
    Params:
        value (:class:`int`)
            The value of the option
        
    """

    ID: str = Field("optionValueInteger", alias="@type")
    value: int

    @staticmethod
    def read(q: dict) -> OptionValueInteger:
        return OptionValueInteger.construct(**q)


class OptionValueString(OptionValue):
    """
    Represents a string option
    
    Params:
        value (:class:`str`)
            The value of the option
        
    """

    ID: str = Field("optionValueString", alias="@type")
    value: str

    @staticmethod
    def read(q: dict) -> OptionValueString:
        return OptionValueString.construct(**q)
