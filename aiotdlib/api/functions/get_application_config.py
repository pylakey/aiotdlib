# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetApplicationConfig(BaseObject):
    """
    Returns application config, provided by the server. Can be called before authorization
    """

    ID: typing.Literal["getApplicationConfig"] = Field("getApplicationConfig", validation_alias="@type", alias="@type")
