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
    
    Params:
        url (:class:`str`)
            Related article URL
        
        title (:class:`str`)
            Article title; may be empty
        
        param_description (:class:`str`)
            Article description; may be empty
        
        photo (:class:`Photo`)
            Article photo; may be null
        
        author (:class:`str`)
            Article author; may be empty
        
        publish_date (:class:`int`)
            Point in time (Unix timestamp) when the article was published; 0 if unknown
        
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
