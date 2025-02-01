# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CreateGroupCall(BaseObject):
    """
    Creates a group call from a one-to-one call

    :param call_id: Call identifier
    :type call_id: :class:`Int32`
    """

    ID: typing.Literal["createGroupCall"] = Field("createGroupCall", validation_alias="@type", alias="@type")
    call_id: Int32
