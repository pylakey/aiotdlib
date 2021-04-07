# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class InputPassportElementErrorSource(BaseObject):
    """
    Contains the description of an error in a Telegram Passport element; for bots only
    
    """

    ID: str = Field("inputPassportElementErrorSource", alias="@type")


class InputPassportElementErrorSourceDataField(InputPassportElementErrorSource):
    """
    A data field contains an error. The error is considered resolved when the field's value changes
    
    Params:
        field_name (:class:`str`)
            Field name
        
        data_hash (:class:`str`)
            Current data hash
        
    """

    ID: str = Field("inputPassportElementErrorSourceDataField", alias="@type")
    field_name: str
    data_hash: str

    @staticmethod
    def read(q: dict) -> InputPassportElementErrorSourceDataField:
        return InputPassportElementErrorSourceDataField.construct(**q)


class InputPassportElementErrorSourceFile(InputPassportElementErrorSource):
    """
    The file contains an error. The error is considered resolved when the file changes
    
    Params:
        file_hash (:class:`str`)
            Current hash of the file which has the error
        
    """

    ID: str = Field("inputPassportElementErrorSourceFile", alias="@type")
    file_hash: str

    @staticmethod
    def read(q: dict) -> InputPassportElementErrorSourceFile:
        return InputPassportElementErrorSourceFile.construct(**q)


class InputPassportElementErrorSourceFiles(InputPassportElementErrorSource):
    """
    The list of attached files contains an error. The error is considered resolved when the file list changes
    
    Params:
        file_hashes (:obj:`list[str]`)
            Current hashes of all attached files
        
    """

    ID: str = Field("inputPassportElementErrorSourceFiles", alias="@type")
    file_hashes: list[str]

    @staticmethod
    def read(q: dict) -> InputPassportElementErrorSourceFiles:
        return InputPassportElementErrorSourceFiles.construct(**q)


class InputPassportElementErrorSourceFrontSide(InputPassportElementErrorSource):
    """
    The front side of the document contains an error. The error is considered resolved when the file with the front side of the document changes
    
    Params:
        file_hash (:class:`str`)
            Current hash of the file containing the front side
        
    """

    ID: str = Field("inputPassportElementErrorSourceFrontSide", alias="@type")
    file_hash: str

    @staticmethod
    def read(q: dict) -> InputPassportElementErrorSourceFrontSide:
        return InputPassportElementErrorSourceFrontSide.construct(**q)


class InputPassportElementErrorSourceReverseSide(InputPassportElementErrorSource):
    """
    The reverse side of the document contains an error. The error is considered resolved when the file with the reverse side of the document changes
    
    Params:
        file_hash (:class:`str`)
            Current hash of the file containing the reverse side
        
    """

    ID: str = Field("inputPassportElementErrorSourceReverseSide", alias="@type")
    file_hash: str

    @staticmethod
    def read(q: dict) -> InputPassportElementErrorSourceReverseSide:
        return InputPassportElementErrorSourceReverseSide.construct(**q)


class InputPassportElementErrorSourceSelfie(InputPassportElementErrorSource):
    """
    The selfie contains an error. The error is considered resolved when the file with the selfie changes
    
    Params:
        file_hash (:class:`str`)
            Current hash of the file containing the selfie
        
    """

    ID: str = Field("inputPassportElementErrorSourceSelfie", alias="@type")
    file_hash: str

    @staticmethod
    def read(q: dict) -> InputPassportElementErrorSourceSelfie:
        return InputPassportElementErrorSourceSelfie.construct(**q)


class InputPassportElementErrorSourceTranslationFile(InputPassportElementErrorSource):
    """
    One of the files containing the translation of the document contains an error. The error is considered resolved when the file with the translation changes
    
    Params:
        file_hash (:class:`str`)
            Current hash of the file containing the translation
        
    """

    ID: str = Field("inputPassportElementErrorSourceTranslationFile", alias="@type")
    file_hash: str

    @staticmethod
    def read(q: dict) -> InputPassportElementErrorSourceTranslationFile:
        return InputPassportElementErrorSourceTranslationFile.construct(**q)


class InputPassportElementErrorSourceTranslationFiles(InputPassportElementErrorSource):
    """
    The translation of the document contains an error. The error is considered resolved when the list of files changes
    
    Params:
        file_hashes (:obj:`list[str]`)
            Current hashes of all files with the translation
        
    """

    ID: str = Field("inputPassportElementErrorSourceTranslationFiles", alias="@type")
    file_hashes: list[str]

    @staticmethod
    def read(q: dict) -> InputPassportElementErrorSourceTranslationFiles:
        return InputPassportElementErrorSourceTranslationFiles.construct(**q)


class InputPassportElementErrorSourceUnspecified(InputPassportElementErrorSource):
    """
    The element contains an error in an unspecified place. The error will be considered resolved when new data is added
    
    Params:
        element_hash (:class:`str`)
            Current hash of the entire element
        
    """

    ID: str = Field("inputPassportElementErrorSourceUnspecified", alias="@type")
    element_hash: str

    @staticmethod
    def read(q: dict) -> InputPassportElementErrorSourceUnspecified:
        return InputPassportElementErrorSourceUnspecified.construct(**q)
