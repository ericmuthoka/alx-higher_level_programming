#!/usr/bin/python3

class LockedClass:
    def __init__(self):
        self._attributes = {}

    def __setattr__(self, name, value):
        if name == "first_name":
            self._attributes[name] = value
        else:
            raise AttributeError(f"Cannot create attribute {name}")

    def __getattribute__(self, name):
        if name in ["_attributes", "__setattr__", "__getattribute__", "__init__"]:
            return super().__getattribute__(name)
        if name in self._attributes:
            return self._attributes[name]
        else:
            raise AttributeError(f"Attribute {name} does not exist")
