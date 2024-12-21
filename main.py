import sys
import getstatus
import update

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        if args[1] == "update":
            update.update()
        elif args[1] == "status":
            getstatus.get_status()
        else:
            print("argument must be 'update' or 'status'")
            sys.exit(1)
    else:
        print("need one argument: 'update' or 'status'") 
        sys.exit(1)