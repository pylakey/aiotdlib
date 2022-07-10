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
    
    :param bio: The new value of the user bio; 0-GetOption("bio_length_max") characters without line feeds
    :type bio: :class:`str`
    
    """

    ID: str = Field("setBio", alias="@type")
    bio: str

    @staticmethod
    def read(q: dict) -> SetBio:
        return SetBio.construct(**q)
