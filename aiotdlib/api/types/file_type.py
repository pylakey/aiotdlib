# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class FileType(BaseObject):
    """
    Represents the type of a file
    
    """

    ID: str = Field("fileType", alias="@type")


class FileTypeAnimation(FileType):
    """
    The file is an animation
    
    """

    ID: str = Field("fileTypeAnimation", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeAnimation:
        return FileTypeAnimation.construct(**q)


class FileTypeAudio(FileType):
    """
    The file is an audio file
    
    """

    ID: str = Field("fileTypeAudio", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeAudio:
        return FileTypeAudio.construct(**q)


class FileTypeDocument(FileType):
    """
    The file is a document
    
    """

    ID: str = Field("fileTypeDocument", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeDocument:
        return FileTypeDocument.construct(**q)


class FileTypeNone(FileType):
    """
    The data is not a file
    
    """

    ID: str = Field("fileTypeNone", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeNone:
        return FileTypeNone.construct(**q)


class FileTypePhoto(FileType):
    """
    The file is a photo
    
    """

    ID: str = Field("fileTypePhoto", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypePhoto:
        return FileTypePhoto.construct(**q)


class FileTypeProfilePhoto(FileType):
    """
    The file is a profile photo
    
    """

    ID: str = Field("fileTypeProfilePhoto", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeProfilePhoto:
        return FileTypeProfilePhoto.construct(**q)


class FileTypeSecret(FileType):
    """
    The file was sent to a secret chat (the file type is not known to the server)
    
    """

    ID: str = Field("fileTypeSecret", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeSecret:
        return FileTypeSecret.construct(**q)


class FileTypeSecretThumbnail(FileType):
    """
    The file is a thumbnail of a file from a secret chat
    
    """

    ID: str = Field("fileTypeSecretThumbnail", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeSecretThumbnail:
        return FileTypeSecretThumbnail.construct(**q)


class FileTypeSecure(FileType):
    """
    The file is a file from Secure storage used for storing Telegram Passport files
    
    """

    ID: str = Field("fileTypeSecure", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeSecure:
        return FileTypeSecure.construct(**q)


class FileTypeSticker(FileType):
    """
    The file is a sticker
    
    """

    ID: str = Field("fileTypeSticker", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeSticker:
        return FileTypeSticker.construct(**q)


class FileTypeThumbnail(FileType):
    """
    The file is a thumbnail of another file
    
    """

    ID: str = Field("fileTypeThumbnail", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeThumbnail:
        return FileTypeThumbnail.construct(**q)


class FileTypeUnknown(FileType):
    """
    The file type is not yet known
    
    """

    ID: str = Field("fileTypeUnknown", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeUnknown:
        return FileTypeUnknown.construct(**q)


class FileTypeVideo(FileType):
    """
    The file is a video
    
    """

    ID: str = Field("fileTypeVideo", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeVideo:
        return FileTypeVideo.construct(**q)


class FileTypeVideoNote(FileType):
    """
    The file is a video note
    
    """

    ID: str = Field("fileTypeVideoNote", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeVideoNote:
        return FileTypeVideoNote.construct(**q)


class FileTypeVoiceNote(FileType):
    """
    The file is a voice note
    
    """

    ID: str = Field("fileTypeVoiceNote", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeVoiceNote:
        return FileTypeVoiceNote.construct(**q)


class FileTypeWallpaper(FileType):
    """
    The file is a wallpaper or a background pattern
    
    """

    ID: str = Field("fileTypeWallpaper", alias="@type")

    @staticmethod
    def read(q: dict) -> FileTypeWallpaper:
        return FileTypeWallpaper.construct(**q)
