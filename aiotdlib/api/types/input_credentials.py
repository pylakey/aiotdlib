# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

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
    
    Params:
        data (:class:`str`)
            JSON-encoded data with the credential identifier
        
    """

    ID: str = Field("inputCredentialsApplePay", alias="@type")
    data: str

    @staticmethod
    def read(q: dict) -> InputCredentialsApplePay:
        return InputCredentialsApplePay.construct(**q)


class InputCredentialsGooglePay(InputCredentials):
    """
    Applies if a user enters new credentials using Google Pay
    
    Params:
        data (:class:`str`)
            JSON-encoded data with the credential identifier
        
    """

    ID: str = Field("inputCredentialsGooglePay", alias="@type")
    data: str

    @staticmethod
    def read(q: dict) -> InputCredentialsGooglePay:
        return InputCredentialsGooglePay.construct(**q)


class InputCredentialsNew(InputCredentials):
    """
    Applies if a user enters new credentials on a payment provider website
    
    Params:
        data (:class:`str`)
            Contains JSON-encoded data with a credential identifier from the payment provider
        
        allow_save (:class:`bool`)
            True, if the credential identifier can be saved on the server side
        
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
    
    Params:
        saved_credentials_id (:class:`str`)
            Identifier of the saved credentials
        
    """

    ID: str = Field("inputCredentialsSaved", alias="@type")
    saved_credentials_id: str

    @staticmethod
    def read(q: dict) -> InputCredentialsSaved:
        return InputCredentialsSaved.construct(**q)
