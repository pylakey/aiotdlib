# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetBio(BaseObject):
    """
    Changes the bio of the current user
    
    Params:
        bio (:class:`str`)
            The new value of the user bio; 0-70 characters without line feeds
        
    """

    ID: str = Field("setBio", alias="@type")
    bio: str

    @staticmethod
    def read(q: dict) -> SetBio:
        return SetBio.construct(**q)
