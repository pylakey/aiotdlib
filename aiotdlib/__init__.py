__version__ = "0.22.0"

import pydantic

if pydantic.VERSION.startswith("2"):
    raise NotImplementedError("Aiotdlib currently does not support Pydantic V2")

from .client import (
    Client,
    ClientOptions,
    ClientParseMode,
    ClientProxySettings,
    ClientProxyType,
)
from .filters import (
    AllFilter,
    AnimationFilter,
    AudioFilter,
    BaseFilter,
    BaseObjectFilter,
    BotCommandFilter,
    ContactFilter,
    DiceFilter,
    DocumentFilter,
    FilterCallable,
    Filters,
    GameFilter,
    InvertedFilter,
    InvoiceFilter,
    LocationFilter,
    MergedFilter,
    MessageFilter,
    PhotoFilter,
    PollFilter,
    RegexFilter,
    StickerFilter,
    TextFilter,
    UnsupportedFilter,
    VenueFilter,
    VideoFilter,
    VideoNoteFilter,
    VoiceNoteFilter,
    XORFilter,
)
from .handlers import (
    Handler,
    HandlerCallable,
)
from .middlewares import MiddlewareCallable
from .tdjson import (
    TDJson,
    TDLibLogVerbosity,
)
from .utils import PendingRequest

__all__ = [
    AllFilter,
    AnimationFilter,
    AudioFilter,
    BaseFilter,
    BaseObjectFilter,
    BotCommandFilter,
    Client,
    ClientOptions,
    ClientParseMode,
    ClientProxySettings,
    ClientProxyType,
    ContactFilter,
    DiceFilter,
    DocumentFilter,
    FilterCallable,
    Filters,
    GameFilter,
    Handler,
    HandlerCallable,
    InvertedFilter,
    InvoiceFilter,
    LocationFilter,
    MergedFilter,
    MessageFilter,
    MiddlewareCallable,
    PendingRequest,
    PhotoFilter,
    PollFilter,
    RegexFilter,
    StickerFilter,
    TDJson,
    TDLibLogVerbosity,
    TextFilter,
    UnsupportedFilter,
    VenueFilter,
    VideoFilter,
    VideoNoteFilter,
    VoiceNoteFilter,
    XORFilter,
]
