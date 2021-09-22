# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GroupCallVideoQuality(BaseObject):
    """
    Describes the quality of a group call video
    
    """

    ID: str = Field("groupCallVideoQuality", alias="@type")


class GroupCallVideoQualityFull(GroupCallVideoQuality):
    """
    The best available video quality
    
    """

    ID: str = Field("groupCallVideoQualityFull", alias="@type")

    @staticmethod
    def read(q: dict) -> GroupCallVideoQualityFull:
        return GroupCallVideoQualityFull.construct(**q)


class GroupCallVideoQualityMedium(GroupCallVideoQuality):
    """
    The medium video quality
    
    """

    ID: str = Field("groupCallVideoQualityMedium", alias="@type")

    @staticmethod
    def read(q: dict) -> GroupCallVideoQualityMedium:
        return GroupCallVideoQualityMedium.construct(**q)


class GroupCallVideoQualityThumbnail(GroupCallVideoQuality):
    """
    The worst available video quality
    
    """

    ID: str = Field("groupCallVideoQualityThumbnail", alias="@type")

    @staticmethod
    def read(q: dict) -> GroupCallVideoQualityThumbnail:
        return GroupCallVideoQualityThumbnail.construct(**q)
