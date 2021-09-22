# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputChatPhoto
from ..base_object import BaseObject


class SetProfilePhoto(BaseObject):
    """
    Changes a profile photo for the current user
    
    :param photo: Profile photo to set
    :type photo: :class:`InputChatPhoto`
    
    """

    ID: str = Field("setProfilePhoto", alias="@type")
    photo: InputChatPhoto

    @staticmethod
    def read(q: dict) -> SetProfilePhoto:
        return SetProfilePhoto.construct(**q)
