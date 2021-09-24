# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatReportReason(BaseObject):
    """
    Describes the reason why a chat is reported
    
    """

    ID: str = Field("chatReportReason", alias="@type")


class ChatReportReasonChildAbuse(ChatReportReason):
    """
    The chat has child abuse related content
    
    """

    ID: str = Field("chatReportReasonChildAbuse", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatReportReasonChildAbuse:
        return ChatReportReasonChildAbuse.construct(**q)


class ChatReportReasonCopyright(ChatReportReason):
    """
    The chat contains copyrighted content
    
    """

    ID: str = Field("chatReportReasonCopyright", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatReportReasonCopyright:
        return ChatReportReasonCopyright.construct(**q)


class ChatReportReasonCustom(ChatReportReason):
    """
    A custom reason provided by the user
    
    """

    ID: str = Field("chatReportReasonCustom", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatReportReasonCustom:
        return ChatReportReasonCustom.construct(**q)


class ChatReportReasonFake(ChatReportReason):
    """
    The chat represents a fake account
    
    """

    ID: str = Field("chatReportReasonFake", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatReportReasonFake:
        return ChatReportReasonFake.construct(**q)


class ChatReportReasonPornography(ChatReportReason):
    """
    The chat contains pornographic messages
    
    """

    ID: str = Field("chatReportReasonPornography", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatReportReasonPornography:
        return ChatReportReasonPornography.construct(**q)


class ChatReportReasonSpam(ChatReportReason):
    """
    The chat contains spam messages
    
    """

    ID: str = Field("chatReportReasonSpam", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatReportReasonSpam:
        return ChatReportReasonSpam.construct(**q)


class ChatReportReasonUnrelatedLocation(ChatReportReason):
    """
    The location-based chat is unrelated to its stated location
    
    """

    ID: str = Field("chatReportReasonUnrelatedLocation", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatReportReasonUnrelatedLocation:
        return ChatReportReasonUnrelatedLocation.construct(**q)


class ChatReportReasonViolence(ChatReportReason):
    """
    The chat promotes violence
    
    """

    ID: str = Field("chatReportReasonViolence", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatReportReasonViolence:
        return ChatReportReasonViolence.construct(**q)
