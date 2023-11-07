# --------------------------------------------------------------------
# __init__.py
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Tuesday November 7, 2023
# --------------------------------------------------------------------

import inspect
from typing import Callable


# --------------------------------------------------------------------
class CommandMap(dict[str, Callable]):
    @staticmethod
    def get_prefixed_methods(prefix, obj):
        return [
            getattr(obj, name)
            for name in dir(obj)
            if name.startswith(prefix) and callable(getattr(obj, name))
        ]

    def __init__(self, obj, prefix="cmd_"):
        self.prefix = prefix
        for method in CommandMap.get_prefixed_methods(self.prefix, obj):
            self.define(method)

    def define(self, f):
        self[f.__name__.removeprefix(self.prefix)] = f

    def signatures(self):
        for key, value in sorted(self.items(), key=lambda x: x[0]):
            yield (key, inspect.signature(value))


# --------------------------------------------------------------------
def commandmap(cls: type, prefix="cmd_") -> type:
    class _CommandMapWrapper(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.commands = CommandMap(self)

    return _CommandMapWrapper
