# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .photo import Photo
from ..base_object import BaseObject


class PageBlockRelatedArticle(BaseObject):
    """
    Contains information about a related article
    
    :param url: Related article URL
    :type url: :class:`str`
    
    :param title: Article title; may be empty
    :type title: :class:`str`
    
    :param param_description: Article description; may be empty
    :type param_description: :class:`str`
    
    :param photo: Article photo; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    
    :param author: Article author; may be empty
    :type author: :class:`str`
    
    :param publish_date: Point in time (Unix timestamp) when the article was published; 0 if unknown
    :type publish_date: :class:`int`
    
    """

    ID: str = Field("pageBlockRelatedArticle", alias="@type")
    url: str
    title: str
    param_description: str
    photo: typing.Optional[Photo] = None
    author: str
    publish_date: int

    @staticmethod
    def read(q: dict) -> PageBlockRelatedArticle:
        return PageBlockRelatedArticle.construct(**q)
