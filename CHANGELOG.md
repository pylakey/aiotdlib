# aiotdlib CHANGELOG

### v0.0.2
* Removed redundant `CurrentAuthorizationState` class

* added `parse_mode` param to `Client` class. 
  Default parse mode for high-level methods like `send_message`. Default: "html"

* `Client.send_message` now automatically parses text entities in text. 
  Text will be parsed according to `parse_mode` option passed in constructor

### v0.0.1 - First Public Release