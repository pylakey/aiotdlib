# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import Contact
from ..base_object import BaseObject


class AddContact(BaseObject):
    """
    Adds a user to the contact list or edits an existing contact by their user identifier
    
    :param contact: The contact to add or edit; phone number can be empty and needs to be specified only if known, vCard is ignored
    :type contact: :class:`Contact`
    
    :param share_phone_number: True, if the new contact needs to be allowed to see current user's phone number. A corresponding rule to userPrivacySettingShowPhoneNumber will be added if needed. Use the field userFullInfo.need_phone_number_privacy_exception to check whether the current user needs to be asked to share their phone number
    :type share_phone_number: :class:`bool`
    
    """

    ID: str = Field("addContact", alias="@type")
    contact: Contact
    share_phone_number: bool

    @staticmethod
    def read(q: dict) -> AddContact:
        return AddContact.construct(**q)
