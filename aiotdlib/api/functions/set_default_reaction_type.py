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

    :param reaction_type: New type of the default reaction
    :type reaction_type: :class:`ReactionType`
    """

    ID: typing.Literal["setDefaultReactionType"] = "setDefaultReactionType"
    reaction_type: ReactionType
