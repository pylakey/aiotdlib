# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    AffiliateProgramSortOrder,
    AffiliateType,
)


class SearchAffiliatePrograms(BaseObject):
    """
    Searches affiliate programs that can be connected to the given affiliate

    :param affiliate: The affiliate for which affiliate programs are searched for
    :type affiliate: :class:`AffiliateType`
    :param sort_order: Sort order for the results
    :type sort_order: :class:`AffiliateProgramSortOrder`
    :param offset: Offset of the first affiliate program to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of affiliate programs to return
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchAffiliatePrograms"] = Field(
        "searchAffiliatePrograms", validation_alias="@type", alias="@type"
    )
    affiliate: AffiliateType
    sort_order: AffiliateProgramSortOrder
    offset: String
    limit: Int32
