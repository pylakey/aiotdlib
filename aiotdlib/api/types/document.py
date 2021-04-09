# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from .minithumbnail import Minithumbnail
from .thumbnail import Thumbnail
from ..base_object import BaseObject


class Document(BaseObject):
    """
    Describes a document of any type
    
    Params:
        file_name (:class:`str`)
            Original name of the file; as defined by the sender
        
        mime_type (:class:`str`)
            MIME type of the file; as defined by the sender
        
        minithumbnail (:class:`Minithumbnail`)
            Document minithumbnail; may be null
        
        thumbnail (:class:`Thumbnail`)
            Document thumbnail in JPEG or PNG format (PNG will be used only for background patterns); as defined by the sender; may be null
        
        document (:class:`File`)
            File containing the document
        
    """

    ID: str = Field("document", alias="@type")
    file_name: str
    mime_type: str
    minithumbnail: typing.Optional[Minithumbnail] = None
    thumbnail: typing.Optional[Thumbnail] = None
    document: File

    @staticmethod
    def read(q: dict) -> Document:
        return Document.construct(**q)
