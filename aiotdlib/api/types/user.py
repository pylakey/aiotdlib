# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .profile_photo import ProfilePhoto
from .user_status import UserStatus
from .user_type import UserType
from ..base_object import BaseObject


class User(BaseObject):
    """
    Represents a user
    
    :param id: User identifier
    :type id: :class:`int`
    
    :param first_name: First name of the user
    :type first_name: :class:`str`
    
    :param last_name: Last name of the user
    :type last_name: :class:`str`
    
    :param username: Username of the user
    :type username: :class:`str`
    
    :param phone_number: Phone number of the user
    :type phone_number: :class:`str`
    
    :param status: Current online status of the user
    :type status: :class:`UserStatus`
    
    :param profile_photo: Profile photo of the user; may be null, defaults to None
    :type profile_photo: :class:`ProfilePhoto`, optional
    
    :param is_contact: The user is a contact of the current user
    :type is_contact: :class:`bool`
    
    :param is_mutual_contact: The user is a contact of the current user and the current user is a contact of the user
    :type is_mutual_contact: :class:`bool`
    
    :param is_verified: True, if the user is verified
    :type is_verified: :class:`bool`
    
    :param is_support: True, if the user is Telegram support account
    :type is_support: :class:`bool`
    
    :param restriction_reason: If non-empty, it contains a human-readable description of the reason why access to this user must be restricted
    :type restriction_reason: :class:`str`
    
    :param is_scam: True, if many users reported this user as a scam
    :type is_scam: :class:`bool`
    
    :param is_fake: True, if many users reported this user as a fake account
    :type is_fake: :class:`bool`
    
    :param have_access: If false, the user is inaccessible, and the only information known about the user is inside this class. It can't be passed to any method except GetUser
    :type have_access: :class:`bool`
    
    :param type_: Type of the user
    :type type_: :class:`UserType`
    
    :param language_code: IETF language tag of the user's language; only available to bots
    :type language_code: :class:`str`
    
    """

    ID: str = Field("user", alias="@type")
    id: int
    first_name: str
    last_name: str
    username: str
    phone_number: str
    status: UserStatus
    profile_photo: typing.Optional[ProfilePhoto] = None
    is_contact: bool
    is_mutual_contact: bool
    is_verified: bool
    is_support: bool
    restriction_reason: str
    is_scam: bool
    is_fake: bool
    have_access: bool
    type_: UserType = Field(..., alias='type')
    language_code: str

    @staticmethod
    def read(q: dict) -> User:
        return User.construct(**q)
