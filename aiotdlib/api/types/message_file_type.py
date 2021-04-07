# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class MessageFileType(BaseObject):
    """
    Contains information about a file with messages exported from another app
    
    """

    ID: str = Field("messageFileType", alias="@type")


class MessageFileTypeGroup(MessageFileType):
    """
    The messages was exported from a group chat
    
    Params:
        title (:class:`str`)
            Title of the group chat; may be empty if unrecognized
        
    """

    ID: str = Field("messageFileTypeGroup", alias="@type")
    title: str

    @staticmethod
    def read(q: dict) -> MessageFileTypeGroup:
        return MessageFileTypeGroup.construct(**q)


class MessageFileTypePrivate(MessageFileType):
    """
    The messages was exported from a private chat
    
    Params:
        name (:class:`str`)
            Name of the other party; may be empty if unrecognized
        
    """

    ID: str = Field("messageFileTypePrivate", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> MessageFileTypePrivate:
        return MessageFileTypePrivate.construct(**q)


class MessageFileTypeUnknown(MessageFileType):
    """
    The messages was exported from a chat of unknown type
    
    """

    ID: str = Field("messageFileTypeUnknown", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageFileTypeUnknown:
        return MessageFileTypeUnknown.construct(**q)
