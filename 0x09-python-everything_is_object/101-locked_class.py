#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, nm, value):
        if nm == "first_name":
            super().__setattr__(nm, value)
        else:
            raise AttributeError(f"'{self.__class__.__name__}'"
                                 f" object has no attribute '{nm}'")
