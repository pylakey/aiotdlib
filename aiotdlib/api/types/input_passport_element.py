# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .address import Address
from .input_identity_document import InputIdentityDocument
from .input_personal_document import InputPersonalDocument
from .personal_details import PersonalDetails
from ..base_object import BaseObject


class InputPassportElement(BaseObject):
    """
    Contains information about a Telegram Passport element to be saved
    
    """

    ID: str = Field("inputPassportElement", alias="@type")


class InputPassportElementAddress(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's address
    
    :param address: The address to be saved
    :type address: :class:`Address`
    
    """

    ID: str = Field("inputPassportElementAddress", alias="@type")
    address: Address

    @staticmethod
    def read(q: dict) -> InputPassportElementAddress:
        return InputPassportElementAddress.construct(**q)


class InputPassportElementBankStatement(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's bank statement
    
    :param bank_statement: The bank statement to be saved
    :type bank_statement: :class:`InputPersonalDocument`
    
    """

    ID: str = Field("inputPassportElementBankStatement", alias="@type")
    bank_statement: InputPersonalDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementBankStatement:
        return InputPassportElementBankStatement.construct(**q)


class InputPassportElementDriverLicense(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's driver license
    
    :param driver_license: The driver license to be saved
    :type driver_license: :class:`InputIdentityDocument`
    
    """

    ID: str = Field("inputPassportElementDriverLicense", alias="@type")
    driver_license: InputIdentityDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementDriverLicense:
        return InputPassportElementDriverLicense.construct(**q)


class InputPassportElementEmailAddress(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's email address
    
    :param email_address: The email address to be saved
    :type email_address: :class:`str`
    
    """

    ID: str = Field("inputPassportElementEmailAddress", alias="@type")
    email_address: str

    @staticmethod
    def read(q: dict) -> InputPassportElementEmailAddress:
        return InputPassportElementEmailAddress.construct(**q)


class InputPassportElementIdentityCard(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's identity card
    
    :param identity_card: The identity card to be saved
    :type identity_card: :class:`InputIdentityDocument`
    
    """

    ID: str = Field("inputPassportElementIdentityCard", alias="@type")
    identity_card: InputIdentityDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementIdentityCard:
        return InputPassportElementIdentityCard.construct(**q)


class InputPassportElementInternalPassport(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's internal passport
    
    :param internal_passport: The internal passport to be saved
    :type internal_passport: :class:`InputIdentityDocument`
    
    """

    ID: str = Field("inputPassportElementInternalPassport", alias="@type")
    internal_passport: InputIdentityDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementInternalPassport:
        return InputPassportElementInternalPassport.construct(**q)


class InputPassportElementPassport(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's passport
    
    :param passport: The passport to be saved
    :type passport: :class:`InputIdentityDocument`
    
    """

    ID: str = Field("inputPassportElementPassport", alias="@type")
    passport: InputIdentityDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementPassport:
        return InputPassportElementPassport.construct(**q)


class InputPassportElementPassportRegistration(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's passport registration
    
    :param passport_registration: The passport registration page to be saved
    :type passport_registration: :class:`InputPersonalDocument`
    
    """

    ID: str = Field("inputPassportElementPassportRegistration", alias="@type")
    passport_registration: InputPersonalDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementPassportRegistration:
        return InputPassportElementPassportRegistration.construct(**q)


class InputPassportElementPersonalDetails(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's personal details
    
    :param personal_details: Personal details of the user
    :type personal_details: :class:`PersonalDetails`
    
    """

    ID: str = Field("inputPassportElementPersonalDetails", alias="@type")
    personal_details: PersonalDetails

    @staticmethod
    def read(q: dict) -> InputPassportElementPersonalDetails:
        return InputPassportElementPersonalDetails.construct(**q)


class InputPassportElementPhoneNumber(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's phone number
    
    :param phone_number: The phone number to be saved
    :type phone_number: :class:`str`
    
    """

    ID: str = Field("inputPassportElementPhoneNumber", alias="@type")
    phone_number: str

    @staticmethod
    def read(q: dict) -> InputPassportElementPhoneNumber:
        return InputPassportElementPhoneNumber.construct(**q)


class InputPassportElementRentalAgreement(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's rental agreement
    
    :param rental_agreement: The rental agreement to be saved
    :type rental_agreement: :class:`InputPersonalDocument`
    
    """

    ID: str = Field("inputPassportElementRentalAgreement", alias="@type")
    rental_agreement: InputPersonalDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementRentalAgreement:
        return InputPassportElementRentalAgreement.construct(**q)


class InputPassportElementTemporaryRegistration(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's temporary registration
    
    :param temporary_registration: The temporary registration document to be saved
    :type temporary_registration: :class:`InputPersonalDocument`
    
    """

    ID: str = Field("inputPassportElementTemporaryRegistration", alias="@type")
    temporary_registration: InputPersonalDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementTemporaryRegistration:
        return InputPassportElementTemporaryRegistration.construct(**q)


class InputPassportElementUtilityBill(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's utility bill
    
    :param utility_bill: The utility bill to be saved
    :type utility_bill: :class:`InputPersonalDocument`
    
    """

    ID: str = Field("inputPassportElementUtilityBill", alias="@type")
    utility_bill: InputPersonalDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementUtilityBill:
        return InputPassportElementUtilityBill.construct(**q)
