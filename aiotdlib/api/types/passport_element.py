# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .address import Address
from .identity_document import IdentityDocument
from .personal_details import PersonalDetails
from .personal_document import PersonalDocument
from ..base_object import BaseObject


class PassportElement(BaseObject):
    """
    Contains information about a Telegram Passport element
    
    """

    ID: str = Field("passportElement", alias="@type")


class PassportElementAddress(PassportElement):
    """
    A Telegram Passport element containing the user's address
    
    :param address: Address
    :type address: :class:`Address`
    
    """

    ID: str = Field("passportElementAddress", alias="@type")
    address: Address

    @staticmethod
    def read(q: dict) -> PassportElementAddress:
        return PassportElementAddress.construct(**q)


class PassportElementBankStatement(PassportElement):
    """
    A Telegram Passport element containing the user's bank statement
    
    :param bank_statement: Bank statement
    :type bank_statement: :class:`PersonalDocument`
    
    """

    ID: str = Field("passportElementBankStatement", alias="@type")
    bank_statement: PersonalDocument

    @staticmethod
    def read(q: dict) -> PassportElementBankStatement:
        return PassportElementBankStatement.construct(**q)


class PassportElementDriverLicense(PassportElement):
    """
    A Telegram Passport element containing the user's driver license
    
    :param driver_license: Driver license
    :type driver_license: :class:`IdentityDocument`
    
    """

    ID: str = Field("passportElementDriverLicense", alias="@type")
    driver_license: IdentityDocument

    @staticmethod
    def read(q: dict) -> PassportElementDriverLicense:
        return PassportElementDriverLicense.construct(**q)


class PassportElementEmailAddress(PassportElement):
    """
    A Telegram Passport element containing the user's email address
    
    :param email_address: Email address
    :type email_address: :class:`str`
    
    """

    ID: str = Field("passportElementEmailAddress", alias="@type")
    email_address: str

    @staticmethod
    def read(q: dict) -> PassportElementEmailAddress:
        return PassportElementEmailAddress.construct(**q)


class PassportElementIdentityCard(PassportElement):
    """
    A Telegram Passport element containing the user's identity card
    
    :param identity_card: Identity card
    :type identity_card: :class:`IdentityDocument`
    
    """

    ID: str = Field("passportElementIdentityCard", alias="@type")
    identity_card: IdentityDocument

    @staticmethod
    def read(q: dict) -> PassportElementIdentityCard:
        return PassportElementIdentityCard.construct(**q)


class PassportElementInternalPassport(PassportElement):
    """
    A Telegram Passport element containing the user's internal passport
    
    :param internal_passport: Internal passport
    :type internal_passport: :class:`IdentityDocument`
    
    """

    ID: str = Field("passportElementInternalPassport", alias="@type")
    internal_passport: IdentityDocument

    @staticmethod
    def read(q: dict) -> PassportElementInternalPassport:
        return PassportElementInternalPassport.construct(**q)


class PassportElementPassport(PassportElement):
    """
    A Telegram Passport element containing the user's passport
    
    :param passport: Passport
    :type passport: :class:`IdentityDocument`
    
    """

    ID: str = Field("passportElementPassport", alias="@type")
    passport: IdentityDocument

    @staticmethod
    def read(q: dict) -> PassportElementPassport:
        return PassportElementPassport.construct(**q)


class PassportElementPassportRegistration(PassportElement):
    """
    A Telegram Passport element containing the user's passport registration pages
    
    :param passport_registration: Passport registration pages
    :type passport_registration: :class:`PersonalDocument`
    
    """

    ID: str = Field("passportElementPassportRegistration", alias="@type")
    passport_registration: PersonalDocument

    @staticmethod
    def read(q: dict) -> PassportElementPassportRegistration:
        return PassportElementPassportRegistration.construct(**q)


class PassportElementPersonalDetails(PassportElement):
    """
    A Telegram Passport element containing the user's personal details
    
    :param personal_details: Personal details of the user
    :type personal_details: :class:`PersonalDetails`
    
    """

    ID: str = Field("passportElementPersonalDetails", alias="@type")
    personal_details: PersonalDetails

    @staticmethod
    def read(q: dict) -> PassportElementPersonalDetails:
        return PassportElementPersonalDetails.construct(**q)


class PassportElementPhoneNumber(PassportElement):
    """
    A Telegram Passport element containing the user's phone number
    
    :param phone_number: Phone number
    :type phone_number: :class:`str`
    
    """

    ID: str = Field("passportElementPhoneNumber", alias="@type")
    phone_number: str

    @staticmethod
    def read(q: dict) -> PassportElementPhoneNumber:
        return PassportElementPhoneNumber.construct(**q)


class PassportElementRentalAgreement(PassportElement):
    """
    A Telegram Passport element containing the user's rental agreement
    
    :param rental_agreement: Rental agreement
    :type rental_agreement: :class:`PersonalDocument`
    
    """

    ID: str = Field("passportElementRentalAgreement", alias="@type")
    rental_agreement: PersonalDocument

    @staticmethod
    def read(q: dict) -> PassportElementRentalAgreement:
        return PassportElementRentalAgreement.construct(**q)


class PassportElementTemporaryRegistration(PassportElement):
    """
    A Telegram Passport element containing the user's temporary registration
    
    :param temporary_registration: Temporary registration
    :type temporary_registration: :class:`PersonalDocument`
    
    """

    ID: str = Field("passportElementTemporaryRegistration", alias="@type")
    temporary_registration: PersonalDocument

    @staticmethod
    def read(q: dict) -> PassportElementTemporaryRegistration:
        return PassportElementTemporaryRegistration.construct(**q)


class PassportElementUtilityBill(PassportElement):
    """
    A Telegram Passport element containing the user's utility bill
    
    :param utility_bill: Utility bill
    :type utility_bill: :class:`PersonalDocument`
    
    """

    ID: str = Field("passportElementUtilityBill", alias="@type")
    utility_bill: PersonalDocument

    @staticmethod
    def read(q: dict) -> PassportElementUtilityBill:
        return PassportElementUtilityBill.construct(**q)
