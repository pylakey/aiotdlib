# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .authentication_code_info import AuthenticationCodeInfo
from .terms_of_service import TermsOfService
from ..base_object import BaseObject


class AuthorizationState(BaseObject):
    """
    Represents the current authorization state of the TDLib client
    
    """

    ID: str = Field("authorizationState", alias="@type")


class AuthorizationStateClosed(AuthorizationState):
    """
    TDLib client is in its final state. All databases are closed and all resources are released. No other updates will be received after this. All queries will be responded to with error code 500. To continue working, one should create a new instance of the TDLib client
    
    """

    ID: str = Field("authorizationStateClosed", alias="@type")

    @staticmethod
    def read(q: dict) -> AuthorizationStateClosed:
        return AuthorizationStateClosed.construct(**q)


class AuthorizationStateClosing(AuthorizationState):
    """
    TDLib is closing, all subsequent queries will be answered with the error 500. Note that closing TDLib can take a while. All resources will be freed only after authorizationStateClosed has been received
    
    """

    ID: str = Field("authorizationStateClosing", alias="@type")

    @staticmethod
    def read(q: dict) -> AuthorizationStateClosing:
        return AuthorizationStateClosing.construct(**q)


class AuthorizationStateLoggingOut(AuthorizationState):
    """
    The user is currently logging out
    
    """

    ID: str = Field("authorizationStateLoggingOut", alias="@type")

    @staticmethod
    def read(q: dict) -> AuthorizationStateLoggingOut:
        return AuthorizationStateLoggingOut.construct(**q)


class AuthorizationStateReady(AuthorizationState):
    """
    The user has been successfully authorized. TDLib is now ready to answer queries
    
    """

    ID: str = Field("authorizationStateReady", alias="@type")

    @staticmethod
    def read(q: dict) -> AuthorizationStateReady:
        return AuthorizationStateReady.construct(**q)


class AuthorizationStateWaitCode(AuthorizationState):
    """
    TDLib needs the user's authentication code to authorize
    
    Params:
        code_info (:class:`AuthenticationCodeInfo`)
            Information about the authorization code that was sent
        
    """

    ID: str = Field("authorizationStateWaitCode", alias="@type")
    code_info: AuthenticationCodeInfo

    @staticmethod
    def read(q: dict) -> AuthorizationStateWaitCode:
        return AuthorizationStateWaitCode.construct(**q)


class AuthorizationStateWaitEncryptionKey(AuthorizationState):
    """
    TDLib needs an encryption key to decrypt the local database
    
    Params:
        is_encrypted (:class:`bool`)
            True, if the database is currently encrypted
        
    """

    ID: str = Field("authorizationStateWaitEncryptionKey", alias="@type")
    is_encrypted: bool

    @staticmethod
    def read(q: dict) -> AuthorizationStateWaitEncryptionKey:
        return AuthorizationStateWaitEncryptionKey.construct(**q)


class AuthorizationStateWaitOtherDeviceConfirmation(AuthorizationState):
    """
    The user needs to confirm authorization on another logged in device by scanning a QR code with the provided link
    
    Params:
        link (:class:`str`)
            A tg:// URL for the QR code. The link will be updated frequently
        
    """

    ID: str = Field("authorizationStateWaitOtherDeviceConfirmation", alias="@type")
    link: str

    @staticmethod
    def read(q: dict) -> AuthorizationStateWaitOtherDeviceConfirmation:
        return AuthorizationStateWaitOtherDeviceConfirmation.construct(**q)


class AuthorizationStateWaitPassword(AuthorizationState):
    """
    The user has been authorized, but needs to enter a password to start using the application
    
    Params:
        password_hint (:class:`str`)
            Hint for the password; may be empty
        
        has_recovery_email_address (:class:`bool`)
            True, if a recovery email address has been set up
        
        recovery_email_address_pattern (:class:`str`)
            Pattern of the email address to which the recovery email was sent; empty until a recovery email has been sent
        
    """

    ID: str = Field("authorizationStateWaitPassword", alias="@type")
    password_hint: str
    has_recovery_email_address: bool
    recovery_email_address_pattern: str

    @staticmethod
    def read(q: dict) -> AuthorizationStateWaitPassword:
        return AuthorizationStateWaitPassword.construct(**q)


class AuthorizationStateWaitPhoneNumber(AuthorizationState):
    """
    TDLib needs the user's phone number to authorize. Call `setAuthenticationPhoneNumber` to provide the phone number, or use `requestQrCodeAuthentication`, or `checkAuthenticationBotToken` for other authentication options
    
    """

    ID: str = Field("authorizationStateWaitPhoneNumber", alias="@type")

    @staticmethod
    def read(q: dict) -> AuthorizationStateWaitPhoneNumber:
        return AuthorizationStateWaitPhoneNumber.construct(**q)


class AuthorizationStateWaitRegistration(AuthorizationState):
    """
    The user is unregistered and need to accept terms of service and enter their first name and last name to finish registration
    
    Params:
        terms_of_service (:class:`TermsOfService`)
            Telegram terms of service
        
    """

    ID: str = Field("authorizationStateWaitRegistration", alias="@type")
    terms_of_service: TermsOfService

    @staticmethod
    def read(q: dict) -> AuthorizationStateWaitRegistration:
        return AuthorizationStateWaitRegistration.construct(**q)


class AuthorizationStateWaitTdlibParameters(AuthorizationState):
    """
    TDLib needs TdlibParameters for initialization
    
    """

    ID: str = Field("authorizationStateWaitTdlibParameters", alias="@type")

    @staticmethod
    def read(q: dict) -> AuthorizationStateWaitTdlibParameters:
        return AuthorizationStateWaitTdlibParameters.construct(**q)
