# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class JsonValue(BaseObject):
    """
    Represents a JSON value
    
    """

    ID: str = Field("jsonValue", alias="@type")


class JsonValueArray(JsonValue):
    """
    Represents a JSON array
    
    Params:
        values (:obj:`list[JsonValue]`)
            The list of array elements
        
    """

    ID: str = Field("jsonValueArray", alias="@type")
    values: list[JsonValue]

    @staticmethod
    def read(q: dict) -> JsonValueArray:
        return JsonValueArray.construct(**q)


class JsonValueBoolean(JsonValue):
    """
    Represents a boolean JSON value
    
    Params:
        value (:class:`bool`)
            The value
        
    """

    ID: str = Field("jsonValueBoolean", alias="@type")
    value: bool

    @staticmethod
    def read(q: dict) -> JsonValueBoolean:
        return JsonValueBoolean.construct(**q)


class JsonValueNull(JsonValue):
    """
    Represents a null JSON value
    
    """

    ID: str = Field("jsonValueNull", alias="@type")

    @staticmethod
    def read(q: dict) -> JsonValueNull:
        return JsonValueNull.construct(**q)


class JsonValueNumber(JsonValue):
    """
    Represents a numeric JSON value
    
    Params:
        value (:class:`float`)
            The value
        
    """

    ID: str = Field("jsonValueNumber", alias="@type")
    value: float

    @staticmethod
    def read(q: dict) -> JsonValueNumber:
        return JsonValueNumber.construct(**q)


class JsonValueObject(JsonValue):
    """
    Represents a JSON object
    
    Params:
        members (:obj:`list[JsonObjectMember]`)
            The list of object members
        
    """

    ID: str = Field("jsonValueObject", alias="@type")
    members: list[JsonObjectMember]

    @staticmethod
    def read(q: dict) -> JsonValueObject:
        return JsonValueObject.construct(**q)


class JsonValueString(JsonValue):
    """
    Represents a string JSON value
    
    Params:
        value (:class:`str`)
            The value
        
    """

    ID: str = Field("jsonValueString", alias="@type")
    value: str

    @staticmethod
    def read(q: dict) -> JsonValueString:
        return JsonValueString.construct(**q)


class JsonObjectMember(BaseObject):
    """
    Represents one member of a JSON object
    
    Params:
        key (:class:`str`)
            Member's key
        
        value (:class:`JsonValue`)
            Member's value
        
    """

    ID: str = Field("jsonObjectMember", alias="@type")
    key: str
    value: JsonValue

    @staticmethod
    def read(q: dict) -> JsonObjectMember:
        return JsonObjectMember.construct(**q)
