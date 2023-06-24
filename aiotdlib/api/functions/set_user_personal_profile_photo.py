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
    InputChatPhoto,
)


class SetUserPersonalProfilePhoto(BaseObject):
    """
    Changes a personal profile photo of a contact user

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param photo: Profile photo to set; pass null to delete the photo; inputChatPhotoPrevious isn't supported in this function, defaults to None
    :type photo: :class:`InputChatPhoto`, optional
    """

    ID: typing.Literal["setUserPersonalProfilePhoto"] = "setUserPersonalProfilePhoto"
    user_id: Int53
    photo: typing.Optional[InputChatPhoto] = None
