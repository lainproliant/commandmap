# CommandMap
A simple decorator function which generates a map of command methods
based on a prefix, by default `cmd_`, on names of methods on an object.

## Example Usage
```python
from commandmap import commandmap, CommandMap
import sys

@commandmap
class CLI(Runnable):
    def cmd_hello(self):
        print("Hello, world!")

class OtherCLI(Runnable):
    def __init__(self):
        self.commands = CommandMap(self)

    def cmd_hello(self):
        print("Hello again, world!")

if __name__ == '__main__':
    cli = CLI()
    other_cli = OtherCLI()

    cli["hello"]()
    other_cli["hello"]()
```

