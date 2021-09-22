# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SavedCredentials(BaseObject):
    """
    Contains information about saved card credentials
    
    :param id: Unique identifier of the saved credentials
    :type id: :class:`str`
    
    :param title: Title of the saved credentials
    :type title: :class:`str`
    
    """

    ID: str = Field("savedCredentials", alias="@type")
    id: str
    title: str

    @staticmethod
    def read(q: dict) -> SavedCredentials:
        return SavedCredentials.construct(**q)
