# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class DeleteProfilePhoto(BaseObject):
    """
    Deletes a profile photo
    
    :param profile_photo_id: Identifier of the profile photo to delete
    :type profile_photo_id: :class:`int`
    
    """

    ID: str = Field("deleteProfilePhoto", alias="@type")
    profile_photo_id: int

    @staticmethod
    def read(q: dict) -> DeleteProfilePhoto:
        return DeleteProfilePhoto.construct(**q)
