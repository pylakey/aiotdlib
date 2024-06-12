# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    BusinessFeature,
)


class GetBusinessFeatures(BaseObject):
    """
    Returns information about features, available to Business users

    :param source: Source of the request; pass null if the method is called from settings or some non-standard source, defaults to None
    :type source: :class:`BusinessFeature`, optional
    """

    ID: typing.Literal["getBusinessFeatures"] = Field("getBusinessFeatures", validation_alias="@type", alias="@type")
    source: typing.Optional[BusinessFeature] = None
