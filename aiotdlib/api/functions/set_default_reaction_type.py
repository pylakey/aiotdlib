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
    ReactionType,
)


class SetDefaultReactionType(BaseObject):
    """
    Changes type of default reaction for the current user

    :param reaction_type: New type of the default reaction. The paid reaction can't be set as default
    :type reaction_type: :class:`ReactionType`
    """

    ID: typing.Literal["setDefaultReactionType"] = Field(
        "setDefaultReactionType", validation_alias="@type", alias="@type"
    )
    reaction_type: ReactionType
