# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

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
    
    Params:
        address (:class:`Address`)
            Address
        
    """

    ID: str = Field("passportElementAddress", alias="@type")
    address: Address

    @staticmethod
    def read(q: dict) -> PassportElementAddress:
        return PassportElementAddress.construct(**q)


class PassportElementBankStatement(PassportElement):
    """
    A Telegram Passport element containing the user's bank statement
    
    Params:
        bank_statement (:class:`PersonalDocument`)
            Bank statement
        
    """

    ID: str = Field("passportElementBankStatement", alias="@type")
    bank_statement: PersonalDocument

    @staticmethod
    def read(q: dict) -> PassportElementBankStatement:
        return PassportElementBankStatement.construct(**q)


class PassportElementDriverLicense(PassportElement):
    """
    A Telegram Passport element containing the user's driver license
    
    Params:
        driver_license (:class:`IdentityDocument`)
            Driver license
        
    """

    ID: str = Field("passportElementDriverLicense", alias="@type")
    driver_license: IdentityDocument

    @staticmethod
    def read(q: dict) -> PassportElementDriverLicense:
        return PassportElementDriverLicense.construct(**q)


class PassportElementEmailAddress(PassportElement):
    """
    A Telegram Passport element containing the user's email address
    
    Params:
        email_address (:class:`str`)
            Email address
        
    """

    ID: str = Field("passportElementEmailAddress", alias="@type")
    email_address: str

    @staticmethod
    def read(q: dict) -> PassportElementEmailAddress:
        return PassportElementEmailAddress.construct(**q)


class PassportElementIdentityCard(PassportElement):
    """
    A Telegram Passport element containing the user's identity card
    
    Params:
        identity_card (:class:`IdentityDocument`)
            Identity card
        
    """

    ID: str = Field("passportElementIdentityCard", alias="@type")
    identity_card: IdentityDocument

    @staticmethod
    def read(q: dict) -> PassportElementIdentityCard:
        return PassportElementIdentityCard.construct(**q)


class PassportElementInternalPassport(PassportElement):
    """
    A Telegram Passport element containing the user's internal passport
    
    Params:
        internal_passport (:class:`IdentityDocument`)
            Internal passport
        
    """

    ID: str = Field("passportElementInternalPassport", alias="@type")
    internal_passport: IdentityDocument

    @staticmethod
    def read(q: dict) -> PassportElementInternalPassport:
        return PassportElementInternalPassport.construct(**q)


class PassportElementPassport(PassportElement):
    """
    A Telegram Passport element containing the user's passport
    
    Params:
        passport (:class:`IdentityDocument`)
            Passport
        
    """

    ID: str = Field("passportElementPassport", alias="@type")
    passport: IdentityDocument

    @staticmethod
    def read(q: dict) -> PassportElementPassport:
        return PassportElementPassport.construct(**q)


class PassportElementPassportRegistration(PassportElement):
    """
    A Telegram Passport element containing the user's passport registration pages
    
    Params:
        passport_registration (:class:`PersonalDocument`)
            Passport registration pages
        
    """

    ID: str = Field("passportElementPassportRegistration", alias="@type")
    passport_registration: PersonalDocument

    @staticmethod
    def read(q: dict) -> PassportElementPassportRegistration:
        return PassportElementPassportRegistration.construct(**q)


class PassportElementPersonalDetails(PassportElement):
    """
    A Telegram Passport element containing the user's personal details
    
    Params:
        personal_details (:class:`PersonalDetails`)
            Personal details of the user
        
    """

    ID: str = Field("passportElementPersonalDetails", alias="@type")
    personal_details: PersonalDetails

    @staticmethod
    def read(q: dict) -> PassportElementPersonalDetails:
        return PassportElementPersonalDetails.construct(**q)


class PassportElementPhoneNumber(PassportElement):
    """
    A Telegram Passport element containing the user's phone number
    
    Params:
        phone_number (:class:`str`)
            Phone number
        
    """

    ID: str = Field("passportElementPhoneNumber", alias="@type")
    phone_number: str

    @staticmethod
    def read(q: dict) -> PassportElementPhoneNumber:
        return PassportElementPhoneNumber.construct(**q)


class PassportElementRentalAgreement(PassportElement):
    """
    A Telegram Passport element containing the user's rental agreement
    
    Params:
        rental_agreement (:class:`PersonalDocument`)
            Rental agreement
        
    """

    ID: str = Field("passportElementRentalAgreement", alias="@type")
    rental_agreement: PersonalDocument

    @staticmethod
    def read(q: dict) -> PassportElementRentalAgreement:
        return PassportElementRentalAgreement.construct(**q)


class PassportElementTemporaryRegistration(PassportElement):
    """
    A Telegram Passport element containing the user's temporary registration
    
    Params:
        temporary_registration (:class:`PersonalDocument`)
            Temporary registration
        
    """

    ID: str = Field("passportElementTemporaryRegistration", alias="@type")
    temporary_registration: PersonalDocument

    @staticmethod
    def read(q: dict) -> PassportElementTemporaryRegistration:
        return PassportElementTemporaryRegistration.construct(**q)


class PassportElementUtilityBill(PassportElement):
    """
    A Telegram Passport element containing the user's utility bill
    
    Params:
        utility_bill (:class:`PersonalDocument`)
            Utility bill
        
    """

    ID: str = Field("passportElementUtilityBill", alias="@type")
    utility_bill: PersonalDocument

    @staticmethod
    def read(q: dict) -> PassportElementUtilityBill:
        return PassportElementUtilityBill.construct(**q)
