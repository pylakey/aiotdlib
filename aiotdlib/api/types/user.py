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
    
    Params:
        id (:class:`int`)
            User identifier
        
        first_name (:class:`str`)
            First name of the user
        
        last_name (:class:`str`)
            Last name of the user
        
        username (:class:`str`)
            Username of the user
        
        phone_number (:class:`str`)
            Phone number of the user
        
        status (:class:`UserStatus`)
            Current online status of the user
        
        profile_photo (:class:`ProfilePhoto`)
            Profile photo of the user; may be null
        
        is_contact (:class:`bool`)
            The user is a contact of the current user
        
        is_mutual_contact (:class:`bool`)
            The user is a contact of the current user and the current user is a contact of the user
        
        is_verified (:class:`bool`)
            True, if the user is verified
        
        is_support (:class:`bool`)
            True, if the user is Telegram support account
        
        restriction_reason (:class:`str`)
            If non-empty, it contains a human-readable description of the reason why access to this user must be restricted
        
        is_scam (:class:`bool`)
            True, if many users reported this user as a scam
        
        is_fake (:class:`bool`)
            True, if many users reported this user as a fake account
        
        have_access (:class:`bool`)
            If false, the user is inaccessible, and the only information known about the user is inside this class. It can't be passed to any method except GetUser
        
        type_ (:class:`UserType`)
            Type of the user
        
        language_code (:class:`str`)
            IETF language tag of the user's language; only available to bots
        
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
