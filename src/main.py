"""Main module for the program.

It takes one argument, either 'update' or 'status'. If 'update' is given, the program will update the status of the user's favorite cryptocurrencies.
If 'status' is given, the program will display the status of the user's favorite cryptocurrencies.
"""
import sys

from status import Status
from update import Updater

ARGUMENT_COUNT = 2

class Main:

    def __init__(self) -> None:
        self.status = Status()
        self.updater = Updater()

    def run(self, args) -> None:
        args = sys.argv
        if len(args) == ARGUMENT_COUNT:
            while True:
                if args[1] == "update":
                    self.updater.update()
                    break
                elif args[1] == "status":
                    self.status.get_status()
                    break
                else:
                    print("argument must be 'update' or 'status'")
                    sys.exit(1)

        else:
            while True:
                print("please enter an argument ('update' or 'status'): ")
                argument = input()
                if argument == "update":
                    self.updater.update()
                    break
                elif argument == "status":
                    self.status.get_status()
                    break
                else:
                    print("argument must be 'update' or 'status'")

if __name__ == "__main__":

    main = Main()
    main.run(sys.argv)
