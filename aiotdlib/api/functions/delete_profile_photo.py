# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteProfilePhoto(BaseObject):
    """
    Deletes a profile photo

    :param profile_photo_id: Identifier of the profile photo to delete
    :type profile_photo_id: :class:`Int64`
    """

    ID: typing.Literal["deleteProfilePhoto"] = "deleteProfilePhoto"
    profile_photo_id: Int64
