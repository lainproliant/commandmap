# --------------------------------------------------------------------
# test.py
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Tuesday November 7, 2023
# --------------------------------------------------------------------

from commandmap import commandmap, CommandMap


# --------------------------------------------------------------------
class Runnable:
    def __init__(self):
        self.commands = dict()

    def run(self):
        self.commands["hello"]()


# --------------------------------------------------------------------
@commandmap
class CLI(Runnable):
    def cmd_hello(self):
        print("Hello, world!")


# --------------------------------------------------------------------
class OtherCLI(Runnable):
    def __init__(self):
        self.commands = CommandMap(self)

    def cmd_hello(self):
        print("Hello again, world!")


# --------------------------------------------------------------------
if __name__ == "__main__":
    cli = CLI()
    other_cli = OtherCLI()

    cli.run()
    other_cli.run()
