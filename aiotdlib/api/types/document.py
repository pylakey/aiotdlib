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
    
    :param file_name: Original name of the file; as defined by the sender
    :type file_name: :class:`str`
    
    :param mime_type: MIME type of the file; as defined by the sender
    :type mime_type: :class:`str`
    
    :param minithumbnail: Document minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    
    :param thumbnail: Document thumbnail in JPEG or PNG format (PNG will be used only for background patterns); as defined by the sender; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
    :param document: File containing the document
    :type document: :class:`File`
    
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
