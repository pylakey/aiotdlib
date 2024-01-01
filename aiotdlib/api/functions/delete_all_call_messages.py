# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteAllCallMessages(BaseObject):
    """
    Deletes all call messages

    :param revoke: Pass true to delete the messages for all users
    :type revoke: :class:`Bool`
    """

    ID: typing.Literal["deleteAllCallMessages"] = Field(
        "deleteAllCallMessages", validation_alias="@type", alias="@type"
    )
    revoke: Bool = False
