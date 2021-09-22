# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class InputCredentials(BaseObject):
    """
    Contains information about the payment method chosen by the user
    
    """

    ID: str = Field("inputCredentials", alias="@type")


class InputCredentialsApplePay(InputCredentials):
    """
    Applies if a user enters new credentials using Apple Pay
    
    :param data: JSON-encoded data with the credential identifier
    :type data: :class:`str`
    
    """

    ID: str = Field("inputCredentialsApplePay", alias="@type")
    data: str

    @staticmethod
    def read(q: dict) -> InputCredentialsApplePay:
        return InputCredentialsApplePay.construct(**q)


class InputCredentialsGooglePay(InputCredentials):
    """
    Applies if a user enters new credentials using Google Pay
    
    :param data: JSON-encoded data with the credential identifier
    :type data: :class:`str`
    
    """

    ID: str = Field("inputCredentialsGooglePay", alias="@type")
    data: str

    @staticmethod
    def read(q: dict) -> InputCredentialsGooglePay:
        return InputCredentialsGooglePay.construct(**q)


class InputCredentialsNew(InputCredentials):
    """
    Applies if a user enters new credentials on a payment provider website
    
    :param data: Contains JSON-encoded data with a credential identifier from the payment provider
    :type data: :class:`str`
    
    :param allow_save: True, if the credential identifier can be saved on the server side
    :type allow_save: :class:`bool`
    
    """

    ID: str = Field("inputCredentialsNew", alias="@type")
    data: str
    allow_save: bool

    @staticmethod
    def read(q: dict) -> InputCredentialsNew:
        return InputCredentialsNew.construct(**q)


class InputCredentialsSaved(InputCredentials):
    """
    Applies if a user chooses some previously saved payment credentials. To use their previously saved credentials, the user must have a valid temporary password
    
    :param saved_credentials_id: Identifier of the saved credentials
    :type saved_credentials_id: :class:`str`
    
    """

    ID: str = Field("inputCredentialsSaved", alias="@type")
    saved_credentials_id: str

    @staticmethod
    def read(q: dict) -> InputCredentialsSaved:
        return InputCredentialsSaved.construct(**q)
