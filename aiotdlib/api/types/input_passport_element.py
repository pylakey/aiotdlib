# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

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
    
    Params:
        address (:class:`Address`)
            The address to be saved
        
    """

    ID: str = Field("inputPassportElementAddress", alias="@type")
    address: Address

    @staticmethod
    def read(q: dict) -> InputPassportElementAddress:
        return InputPassportElementAddress.construct(**q)


class InputPassportElementBankStatement(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's bank statement
    
    Params:
        bank_statement (:class:`InputPersonalDocument`)
            The bank statement to be saved
        
    """

    ID: str = Field("inputPassportElementBankStatement", alias="@type")
    bank_statement: InputPersonalDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementBankStatement:
        return InputPassportElementBankStatement.construct(**q)


class InputPassportElementDriverLicense(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's driver license
    
    Params:
        driver_license (:class:`InputIdentityDocument`)
            The driver license to be saved
        
    """

    ID: str = Field("inputPassportElementDriverLicense", alias="@type")
    driver_license: InputIdentityDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementDriverLicense:
        return InputPassportElementDriverLicense.construct(**q)


class InputPassportElementEmailAddress(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's email address
    
    Params:
        email_address (:class:`str`)
            The email address to be saved
        
    """

    ID: str = Field("inputPassportElementEmailAddress", alias="@type")
    email_address: str

    @staticmethod
    def read(q: dict) -> InputPassportElementEmailAddress:
        return InputPassportElementEmailAddress.construct(**q)


class InputPassportElementIdentityCard(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's identity card
    
    Params:
        identity_card (:class:`InputIdentityDocument`)
            The identity card to be saved
        
    """

    ID: str = Field("inputPassportElementIdentityCard", alias="@type")
    identity_card: InputIdentityDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementIdentityCard:
        return InputPassportElementIdentityCard.construct(**q)


class InputPassportElementInternalPassport(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's internal passport
    
    Params:
        internal_passport (:class:`InputIdentityDocument`)
            The internal passport to be saved
        
    """

    ID: str = Field("inputPassportElementInternalPassport", alias="@type")
    internal_passport: InputIdentityDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementInternalPassport:
        return InputPassportElementInternalPassport.construct(**q)


class InputPassportElementPassport(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's passport
    
    Params:
        passport (:class:`InputIdentityDocument`)
            The passport to be saved
        
    """

    ID: str = Field("inputPassportElementPassport", alias="@type")
    passport: InputIdentityDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementPassport:
        return InputPassportElementPassport.construct(**q)


class InputPassportElementPassportRegistration(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's passport registration
    
    Params:
        passport_registration (:class:`InputPersonalDocument`)
            The passport registration page to be saved
        
    """

    ID: str = Field("inputPassportElementPassportRegistration", alias="@type")
    passport_registration: InputPersonalDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementPassportRegistration:
        return InputPassportElementPassportRegistration.construct(**q)


class InputPassportElementPersonalDetails(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's personal details
    
    Params:
        personal_details (:class:`PersonalDetails`)
            Personal details of the user
        
    """

    ID: str = Field("inputPassportElementPersonalDetails", alias="@type")
    personal_details: PersonalDetails

    @staticmethod
    def read(q: dict) -> InputPassportElementPersonalDetails:
        return InputPassportElementPersonalDetails.construct(**q)


class InputPassportElementPhoneNumber(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's phone number
    
    Params:
        phone_number (:class:`str`)
            The phone number to be saved
        
    """

    ID: str = Field("inputPassportElementPhoneNumber", alias="@type")
    phone_number: str

    @staticmethod
    def read(q: dict) -> InputPassportElementPhoneNumber:
        return InputPassportElementPhoneNumber.construct(**q)


class InputPassportElementRentalAgreement(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's rental agreement
    
    Params:
        rental_agreement (:class:`InputPersonalDocument`)
            The rental agreement to be saved
        
    """

    ID: str = Field("inputPassportElementRentalAgreement", alias="@type")
    rental_agreement: InputPersonalDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementRentalAgreement:
        return InputPassportElementRentalAgreement.construct(**q)


class InputPassportElementTemporaryRegistration(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's temporary registration
    
    Params:
        temporary_registration (:class:`InputPersonalDocument`)
            The temporary registration document to be saved
        
    """

    ID: str = Field("inputPassportElementTemporaryRegistration", alias="@type")
    temporary_registration: InputPersonalDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementTemporaryRegistration:
        return InputPassportElementTemporaryRegistration.construct(**q)


class InputPassportElementUtilityBill(InputPassportElement):
    """
    A Telegram Passport element to be saved containing the user's utility bill
    
    Params:
        utility_bill (:class:`InputPersonalDocument`)
            The utility bill to be saved
        
    """

    ID: str = Field("inputPassportElementUtilityBill", alias="@type")
    utility_bill: InputPersonalDocument

    @staticmethod
    def read(q: dict) -> InputPassportElementUtilityBill:
        return InputPassportElementUtilityBill.construct(**q)
