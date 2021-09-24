# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PassportElementType(BaseObject):
    """
    Contains the type of a Telegram Passport element
    
    """

    ID: str = Field("passportElementType", alias="@type")


class PassportElementTypeAddress(PassportElementType):
    """
    A Telegram Passport element containing the user's address
    
    """

    ID: str = Field("passportElementTypeAddress", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypeAddress:
        return PassportElementTypeAddress.construct(**q)


class PassportElementTypeBankStatement(PassportElementType):
    """
    A Telegram Passport element containing the user's bank statement
    
    """

    ID: str = Field("passportElementTypeBankStatement", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypeBankStatement:
        return PassportElementTypeBankStatement.construct(**q)


class PassportElementTypeDriverLicense(PassportElementType):
    """
    A Telegram Passport element containing the user's driver license
    
    """

    ID: str = Field("passportElementTypeDriverLicense", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypeDriverLicense:
        return PassportElementTypeDriverLicense.construct(**q)


class PassportElementTypeEmailAddress(PassportElementType):
    """
    A Telegram Passport element containing the user's email address
    
    """

    ID: str = Field("passportElementTypeEmailAddress", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypeEmailAddress:
        return PassportElementTypeEmailAddress.construct(**q)


class PassportElementTypeIdentityCard(PassportElementType):
    """
    A Telegram Passport element containing the user's identity card
    
    """

    ID: str = Field("passportElementTypeIdentityCard", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypeIdentityCard:
        return PassportElementTypeIdentityCard.construct(**q)


class PassportElementTypeInternalPassport(PassportElementType):
    """
    A Telegram Passport element containing the user's internal passport
    
    """

    ID: str = Field("passportElementTypeInternalPassport", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypeInternalPassport:
        return PassportElementTypeInternalPassport.construct(**q)


class PassportElementTypePassport(PassportElementType):
    """
    A Telegram Passport element containing the user's passport
    
    """

    ID: str = Field("passportElementTypePassport", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypePassport:
        return PassportElementTypePassport.construct(**q)


class PassportElementTypePassportRegistration(PassportElementType):
    """
    A Telegram Passport element containing the registration page of the user's passport
    
    """

    ID: str = Field("passportElementTypePassportRegistration", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypePassportRegistration:
        return PassportElementTypePassportRegistration.construct(**q)


class PassportElementTypePersonalDetails(PassportElementType):
    """
    A Telegram Passport element containing the user's personal details
    
    """

    ID: str = Field("passportElementTypePersonalDetails", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypePersonalDetails:
        return PassportElementTypePersonalDetails.construct(**q)


class PassportElementTypePhoneNumber(PassportElementType):
    """
    A Telegram Passport element containing the user's phone number
    
    """

    ID: str = Field("passportElementTypePhoneNumber", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypePhoneNumber:
        return PassportElementTypePhoneNumber.construct(**q)


class PassportElementTypeRentalAgreement(PassportElementType):
    """
    A Telegram Passport element containing the user's rental agreement
    
    """

    ID: str = Field("passportElementTypeRentalAgreement", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypeRentalAgreement:
        return PassportElementTypeRentalAgreement.construct(**q)


class PassportElementTypeTemporaryRegistration(PassportElementType):
    """
    A Telegram Passport element containing the user's temporary registration
    
    """

    ID: str = Field("passportElementTypeTemporaryRegistration", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypeTemporaryRegistration:
        return PassportElementTypeTemporaryRegistration.construct(**q)


class PassportElementTypeUtilityBill(PassportElementType):
    """
    A Telegram Passport element containing the user's utility bill
    
    """

    ID: str = Field("passportElementTypeUtilityBill", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementTypeUtilityBill:
        return PassportElementTypeUtilityBill.construct(**q)
