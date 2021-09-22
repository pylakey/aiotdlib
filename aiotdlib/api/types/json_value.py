# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

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
    
    :param values: The list of array elements
    :type values: :class:`list[JsonValue]`
    
    """

    ID: str = Field("jsonValueArray", alias="@type")
    values: list[JsonValue]

    @staticmethod
    def read(q: dict) -> JsonValueArray:
        return JsonValueArray.construct(**q)


class JsonValueBoolean(JsonValue):
    """
    Represents a boolean JSON value
    
    :param value: The value
    :type value: :class:`bool`
    
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
    
    :param value: The value
    :type value: :class:`float`
    
    """

    ID: str = Field("jsonValueNumber", alias="@type")
    value: float

    @staticmethod
    def read(q: dict) -> JsonValueNumber:
        return JsonValueNumber.construct(**q)


class JsonValueObject(JsonValue):
    """
    Represents a JSON object
    
    :param members: The list of object members
    :type members: :class:`list[JsonObjectMember]`
    
    """

    ID: str = Field("jsonValueObject", alias="@type")
    members: list[JsonObjectMember]

    @staticmethod
    def read(q: dict) -> JsonValueObject:
        return JsonValueObject.construct(**q)


class JsonValueString(JsonValue):
    """
    Represents a string JSON value
    
    :param value: The value
    :type value: :class:`str`
    
    """

    ID: str = Field("jsonValueString", alias="@type")
    value: str

    @staticmethod
    def read(q: dict) -> JsonValueString:
        return JsonValueString.construct(**q)


class JsonObjectMember(BaseObject):
    """
    Represents one member of a JSON object
    
    :param key: Member's key
    :type key: :class:`str`
    
    :param value: Member's value
    :type value: :class:`JsonValue`
    
    """

    ID: str = Field("jsonObjectMember", alias="@type")
    key: str
    value: JsonValue

    @staticmethod
    def read(q: dict) -> JsonObjectMember:
        return JsonObjectMember.construct(**q)
