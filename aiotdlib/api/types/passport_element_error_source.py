# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PassportElementErrorSource(BaseObject):
    """
    Contains the description of an error in a Telegram Passport element
    
    """

    ID: str = Field("passportElementErrorSource", alias="@type")


class PassportElementErrorSourceDataField(PassportElementErrorSource):
    """
    One of the data fields contains an error. The error will be considered resolved when the value of the field changes
    
    Params:
        field_name (:class:`str`)
            Field name
        
    """

    ID: str = Field("passportElementErrorSourceDataField", alias="@type")
    field_name: str

    @staticmethod
    def read(q: dict) -> PassportElementErrorSourceDataField:
        return PassportElementErrorSourceDataField.construct(**q)


class PassportElementErrorSourceFile(PassportElementErrorSource):
    """
    The file contains an error. The error will be considered resolved when the file changes
    
    Params:
        file_index (:class:`int`)
            Index of a file with the error
        
    """

    ID: str = Field("passportElementErrorSourceFile", alias="@type")
    file_index: int

    @staticmethod
    def read(q: dict) -> PassportElementErrorSourceFile:
        return PassportElementErrorSourceFile.construct(**q)


class PassportElementErrorSourceFiles(PassportElementErrorSource):
    """
    The list of attached files contains an error. The error will be considered resolved when the list of files changes
    
    """

    ID: str = Field("passportElementErrorSourceFiles", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementErrorSourceFiles:
        return PassportElementErrorSourceFiles.construct(**q)


class PassportElementErrorSourceFrontSide(PassportElementErrorSource):
    """
    The front side of the document contains an error. The error will be considered resolved when the file with the front side changes
    
    """

    ID: str = Field("passportElementErrorSourceFrontSide", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementErrorSourceFrontSide:
        return PassportElementErrorSourceFrontSide.construct(**q)


class PassportElementErrorSourceReverseSide(PassportElementErrorSource):
    """
    The reverse side of the document contains an error. The error will be considered resolved when the file with the reverse side changes
    
    """

    ID: str = Field("passportElementErrorSourceReverseSide", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementErrorSourceReverseSide:
        return PassportElementErrorSourceReverseSide.construct(**q)


class PassportElementErrorSourceSelfie(PassportElementErrorSource):
    """
    The selfie with the document contains an error. The error will be considered resolved when the file with the selfie changes
    
    """

    ID: str = Field("passportElementErrorSourceSelfie", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementErrorSourceSelfie:
        return PassportElementErrorSourceSelfie.construct(**q)


class PassportElementErrorSourceTranslationFile(PassportElementErrorSource):
    """
    One of files with the translation of the document contains an error. The error will be considered resolved when the file changes
    
    Params:
        file_index (:class:`int`)
            Index of a file with the error
        
    """

    ID: str = Field("passportElementErrorSourceTranslationFile", alias="@type")
    file_index: int

    @staticmethod
    def read(q: dict) -> PassportElementErrorSourceTranslationFile:
        return PassportElementErrorSourceTranslationFile.construct(**q)


class PassportElementErrorSourceTranslationFiles(PassportElementErrorSource):
    """
    The translation of the document contains an error. The error will be considered resolved when the list of translation files changes
    
    """

    ID: str = Field("passportElementErrorSourceTranslationFiles", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementErrorSourceTranslationFiles:
        return PassportElementErrorSourceTranslationFiles.construct(**q)


class PassportElementErrorSourceUnspecified(PassportElementErrorSource):
    """
    The element contains an error in an unspecified place. The error will be considered resolved when new data is added
    
    """

    ID: str = Field("passportElementErrorSourceUnspecified", alias="@type")

    @staticmethod
    def read(q: dict) -> PassportElementErrorSourceUnspecified:
        return PassportElementErrorSourceUnspecified.construct(**q)
