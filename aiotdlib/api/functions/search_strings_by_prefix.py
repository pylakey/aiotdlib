# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchStringsByPrefix(BaseObject):
    """
    Searches specified query by word prefixes in the provided strings. Returns 0-based positions of strings that matched. Can be called synchronously

    :param strings: The strings to search in for the query
    :type strings: :class:`Vector[String]`
    :param query: Query to search for
    :type query: :class:`String`
    :param limit: The maximum number of objects to return
    :type limit: :class:`Int32`
    :param return_none_for_empty_query: Pass true to receive no results for an empty query
    :type return_none_for_empty_query: :class:`Bool`
    """

    ID: typing.Literal["searchStringsByPrefix"] = "searchStringsByPrefix"
    strings: Vector[String]
    query: String
    limit: Int32
    return_none_for_empty_query: Bool = False
