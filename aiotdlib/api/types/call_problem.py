# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CallProblem(BaseObject):
    """
    Describes the exact type of a problem with a call
    
    """

    ID: str = Field("callProblem", alias="@type")


class CallProblemDistortedSpeech(CallProblem):
    """
    The speech was distorted
    
    """

    ID: str = Field("callProblemDistortedSpeech", alias="@type")

    @staticmethod
    def read(q: dict) -> CallProblemDistortedSpeech:
        return CallProblemDistortedSpeech.construct(**q)


class CallProblemDistortedVideo(CallProblem):
    """
    The video was distorted
    
    """

    ID: str = Field("callProblemDistortedVideo", alias="@type")

    @staticmethod
    def read(q: dict) -> CallProblemDistortedVideo:
        return CallProblemDistortedVideo.construct(**q)


class CallProblemDropped(CallProblem):
    """
    The call ended unexpectedly
    
    """

    ID: str = Field("callProblemDropped", alias="@type")

    @staticmethod
    def read(q: dict) -> CallProblemDropped:
        return CallProblemDropped.construct(**q)


class CallProblemEcho(CallProblem):
    """
    The user heard their own voice
    
    """

    ID: str = Field("callProblemEcho", alias="@type")

    @staticmethod
    def read(q: dict) -> CallProblemEcho:
        return CallProblemEcho.construct(**q)


class CallProblemInterruptions(CallProblem):
    """
    The other side kept disappearing
    
    """

    ID: str = Field("callProblemInterruptions", alias="@type")

    @staticmethod
    def read(q: dict) -> CallProblemInterruptions:
        return CallProblemInterruptions.construct(**q)


class CallProblemNoise(CallProblem):
    """
    The user heard background noise
    
    """

    ID: str = Field("callProblemNoise", alias="@type")

    @staticmethod
    def read(q: dict) -> CallProblemNoise:
        return CallProblemNoise.construct(**q)


class CallProblemPixelatedVideo(CallProblem):
    """
    The video was pixelated
    
    """

    ID: str = Field("callProblemPixelatedVideo", alias="@type")

    @staticmethod
    def read(q: dict) -> CallProblemPixelatedVideo:
        return CallProblemPixelatedVideo.construct(**q)


class CallProblemSilentLocal(CallProblem):
    """
    The user couldn't hear the other side
    
    """

    ID: str = Field("callProblemSilentLocal", alias="@type")

    @staticmethod
    def read(q: dict) -> CallProblemSilentLocal:
        return CallProblemSilentLocal.construct(**q)


class CallProblemSilentRemote(CallProblem):
    """
    The other side couldn't hear the user
    
    """

    ID: str = Field("callProblemSilentRemote", alias="@type")

    @staticmethod
    def read(q: dict) -> CallProblemSilentRemote:
        return CallProblemSilentRemote.construct(**q)
