#!/usr/bin/python3
"""Console entry Module"""
import cmd


class AirBnbShell(cmd.Cmd):
    """AirBnb shell"""

    intro = "Welcome to the airbnb shell. Type help or ? to list commands.\n"
    prompt = "(airbnb) "
    file = None

    # ----- basic turtle commands -----
    def do_print_args(self, arg):
        "Move the turtle forward by the specified distance:  FORWARD 10"
        print(*parse(arg))


def parse(arg):
    "Convert a series of zero or more numbers to an argument tuple"
    return tuple(map(str, arg.split()))


if __name__ == "__main__":
    AirBnbShell().cmdloop()
