# aiotdlib CHANGELOG

### v0.1.0

#### Added

* Cache mechanism for chats, users and both types of groups
* New high-level API method `Client.get_main_list_chats(limit: int)` - Returns an ordered list of chats in a main chat
  list.
* Multiple raw methods wrappers which work the same but returns cached entity if it was found in cache: `get_chat`
  , `get_user`, `get_user_full_info`, `get_basic_group`, `get_basic_group_full_info`, `get_supergroup`
  , `get_supergroup_full_info`, `get_secret_chat`
* TL Schema parser now parses some parameters constraints in TL Schema such as nullability of parameter, min and max
  length

#### Updated

* API objects were regenerated with updated parser

### v0.0.2

#### Added

* added `parse_mode` param to `Client` class. Default parse mode for high-level methods like `send_message`. Default: "
  html"

#### Updated

* `Client.send_message` now automatically parses text entities in text. Text will be parsed according to `parse_mode`
  option passed in constructor

#### Removed

* Removed redundant `CurrentAuthorizationState` class

### v0.0.1 - First Public Release