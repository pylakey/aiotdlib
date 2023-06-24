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


class SetProfilePhoto(BaseObject):
    """
    Changes a profile photo for the current user

    :param photo: Profile photo to set
    :type photo: :class:`InputChatPhoto`
    :param is_public: Pass true to set a public photo, which will be visible even the main photo is hidden by privacy settings
    :type is_public: :class:`Bool`
    """

    ID: typing.Literal["setProfilePhoto"] = "setProfilePhoto"
    photo: InputChatPhoto
    is_public: Bool = False
