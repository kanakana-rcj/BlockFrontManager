"""Main module for the program.

It takes one argument, either 'update' or 'status'. If 'update' is given, the program will update the status of the user's favorite cryptocurrencies.
If 'status' is given, the program will display the status of the user's favorite cryptocurrencies.
"""
import sys

import getstatus
import update

ARGUMENT_COUNT = 2

if __name__ == "__main__":
    args = sys.argv
    if len(args) == ARGUMENT_COUNT:
        while True:
            if args[1] == "update":
                update.update()
                break
            elif args[1] == "status":
                getstatus.get_status()
                break
            else:
                print("argument must be 'update' or 'status'")
                sys.exit(1)

    else:
        while True:
            print("please enter an argument ('update' or 'status'): ")
            argument = input()
            if argument == "update":
                update.update()
                break
            elif argument == "status":
                getstatus.get_status()
                break
            else:
                print("argument must be 'update' or 'status'")
