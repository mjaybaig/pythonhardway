# Find tool
# format: 
# find.py <dirname> -name "*.txt" 
# args: -name, -type, -print, -exec
# a 45-minute challenge to implement as much of the "find" linux comand as possible
# Author: M Jameel Baig


# 1. gather command line arguments
# 2. first argument is the path to open. store it in a variable
# 3. open that given directory
# 5. if we have the name arg, then filter out those files that have that name
# 4. if we have the type arg, then filter out those that have that type
# 5. print them
# 5. Execute a command on them. command is after the -exec argument

import os
import argparse
import sys
import glob

def main():
    parser = argparse.ArgumentParser(description="find files in a given directory")
    parser.add_argument('targetdir', help="Directory to open", type=str)
    parser.add_argument('-name', dest='targetname', help="name of target file should be like", type=str)
    parser.add_argument('-exec', dest='execcmd', help="command to execute", type=str, nargs='+')

    args = parser.parse_args()

    print(args)
    # print(args.targetdir)
    # open targetdir and get all file names using os.listdir
    targetfiles = os.listdir(args.targetdir)

    # if -name arg exists, filter out all files following -name using glob
    if(args.targetname and len(args.targetname) > 0):
        targetfiles = glob.glob(args.targetname)
        # print(args.targetname)
    print(targetfiles)

    # execute a command for all these files using subprocess
    cmd = args.execcmd
    
    print(cmd)

if __name__ == "__main__":
    main()