# grep.py: A 45-minute challenge to implement as much of grep as possible
# #################CURRENTLY INCOMPLETE##################################
import sys
import os
import re


def main():
    args = sys.argv[1:]
    # print(args)

    fname = args[1]
    file_to_search = open(fname)

    flines = file_to_search.readlines()
    pattern = args[0]

    # We have the lines of the file. We also have the pattern. Now let's find the pattern

    matches = []

    for line in flines:
        if len(re.findall(pattern, line)) > 0:
            matches.append(line)
            continue
        else:
            matches.append([])
        # end if
    # end for

    # print(matches)
    for i, m in enumerate(matches):
        if m != []:
            print(f'{i}: {m}')

# end main


if __name__ == "__main__":
    main()