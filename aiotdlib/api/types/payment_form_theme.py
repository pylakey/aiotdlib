# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PaymentFormTheme(BaseObject):
    """
    Theme colors for a payment form
    
    Params:
        background_color (:class:`int`)
            A color of the payment form background in the RGB24 format
        
        text_color (:class:`int`)
            A color of text in the RGB24 format
        
        hint_color (:class:`int`)
            A color of hints in the RGB24 format
        
        link_color (:class:`int`)
            A color of links in the RGB24 format
        
        button_color (:class:`int`)
            A color of thebuttons in the RGB24 format
        
        button_text_color (:class:`int`)
            A color of text on the buttons in the RGB24 format
        
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
