# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class DeleteAllCallMessages(BaseObject):
    """
    Deletes all call messages
    
    :param revoke: Pass true to delete the messages for all users
    :type revoke: :class:`bool`
    
    """

    ID: str = Field("deleteAllCallMessages", alias="@type")
    revoke: bool

    @staticmethod
    def read(q: dict) -> DeleteAllCallMessages:
        return DeleteAllCallMessages.construct(**q)
