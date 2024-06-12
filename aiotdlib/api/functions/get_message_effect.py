# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessageEffect(BaseObject):
    """
    Returns information about a message effect. Returns a 404 error if the effect is not found

    :param effect_id: Unique identifier of the effect
    :type effect_id: :class:`Int64`
    """

    ID: typing.Literal["getMessageEffect"] = Field("getMessageEffect", validation_alias="@type", alias="@type")
    effect_id: Int64
