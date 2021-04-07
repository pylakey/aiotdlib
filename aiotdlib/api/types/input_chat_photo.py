# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .input_file import InputFile
from ..base_object import BaseObject


class InputChatPhoto(BaseObject):
    """
    Describes a photo to be set as a user profile or chat photo
    
    """

    ID: str = Field("inputChatPhoto", alias="@type")


class InputChatPhotoAnimation(InputChatPhoto):
    """
    An animation in MPEG4 format; must be square, at most 10 seconds long, have width between 160 and 800 and be at most 2MB in size
    
    Params:
        animation (:class:`InputFile`)
            Animation to be set as profile photo. Only inputFileLocal and inputFileGenerated are allowed
        
        main_frame_timestamp (:class:`float`)
            Timestamp of the frame, which will be used as static chat photo
        
    """

    ID: str = Field("inputChatPhotoAnimation", alias="@type")
    animation: InputFile
    main_frame_timestamp: float

    @staticmethod
    def read(q: dict) -> InputChatPhotoAnimation:
        return InputChatPhotoAnimation.construct(**q)


class InputChatPhotoPrevious(InputChatPhoto):
    """
    A previously used profile photo of the current user
    
    Params:
        chat_photo_id (:class:`int`)
            Identifier of the current user's profile photo to reuse
        
    """

    ID: str = Field("inputChatPhotoPrevious", alias="@type")
    chat_photo_id: int

    @staticmethod
    def read(q: dict) -> InputChatPhotoPrevious:
        return InputChatPhotoPrevious.construct(**q)


class InputChatPhotoStatic(InputChatPhoto):
    """
    A static photo in JPEG format
    
    Params:
        photo (:class:`InputFile`)
            Photo to be set as profile photo. Only inputFileLocal and inputFileGenerated are allowed
        
    """

    ID: str = Field("inputChatPhotoStatic", alias="@type")
    photo: InputFile

    @staticmethod
    def read(q: dict) -> InputChatPhotoStatic:
        return InputChatPhotoStatic.construct(**q)
