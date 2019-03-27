# cmdarg.py - an exercise to familarise myself with command line arguments in python
import sys

def main():
    # print(sys.argv)
    helpcmd = ['-h', '-help']

    flags = {
        'flightMode': False,
        'lowBattery': False,
        'headset': False
    }

    recargs = {
        'userName' : '',
        'numBooks' : 0,
        'food' : ''
    }

    flagKeys = list(flags.keys())
    # print(flagKeys)
    args = sys.argv

    for hlp in helpcmd:
        if hlp in args:

            print("This is the help section. Please use carefully")
            return
        # end if
    # end for
    i = 0
    for arg in args:
        # print(arg)
        if arg in flagKeys:
            flags[arg] = not flags[arg]
        elif arg in recargs:
            recargs[arg] = args[i+1]
        i += 1
    # print(recargs)
    # end for
    # print(flags)
    if len(recargs['userName']) > 0:
        print(f"Welcome, {recargs['userName']}")
    if flags['flightMode']:
        print("Have a safe flight!")
    if flags['lowBattery']:
        print("Caution! Low battery")
    if flags['headset']:
        print("Enjoy your music")


    


if __name__ == "__main__":
    main()
