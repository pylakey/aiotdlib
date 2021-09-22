# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class PaymentFormTheme(BaseObject):
    """
    Theme colors for a payment form
    
    :param background_color: A color of the payment form background in the RGB24 format
    :type background_color: :class:`int`
    
    :param text_color: A color of text in the RGB24 format
    :type text_color: :class:`int`
    
    :param hint_color: A color of hints in the RGB24 format
    :type hint_color: :class:`int`
    
    :param link_color: A color of links in the RGB24 format
    :type link_color: :class:`int`
    
    :param button_color: A color of thebuttons in the RGB24 format
    :type button_color: :class:`int`
    
    :param button_text_color: A color of text on the buttons in the RGB24 format
    :type button_text_color: :class:`int`
    
    """

    ID: str = Field("paymentFormTheme", alias="@type")
    background_color: int
    text_color: int
    hint_color: int
    link_color: int
    button_color: int
    button_text_color: int

    @staticmethod
    def read(q: dict) -> PaymentFormTheme:
        return PaymentFormTheme.construct(**q)
