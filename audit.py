###################################################
# FIT9133 Assignment 2 Task 1
# Created by Muhammad Jameel Baig - 29822726
# On 19-SEP-2018
# last modified on 12-OCT-2018
###################################################
# This file perfroms data-cleaning on CHAT files seperated by group
# and outputs the clean data into new files
###################################################
from typing import List, Dict
# Some base variables
groupTD = "TD"
groupSLI = "SLI"

# root of the folder the data is kept in
dataDir = "./ENNI Dataset"

# dictionary holding all the unprocessed TD file contents as a list of lines
# the key for each file will be the name of the file eg "'TD-1' will be the key for the list containing all lines of
# td-1
tdFileContents = {}

# similarly, a list for SLI files
sliFileContents = {}


# This function will read all the files into the two dictionaries we have
# It iterates over the TD and SLI and uploads all TD files before uploading all SLI files
def read_files():
    # Iterate over a couple of tuples containing
    # 1. the group TD/SLI while is used to form the file name etc
    # 2. the destination dictionary that the each file will be kept in
    for group in [(groupTD, tdFileContents), (groupSLI, sliFileContents)]:
        fileno = 1
        # unpacking the current tuple
        grouptype, datadict = group
        # set the base directory
        basedirtemp = f"{dataDir}/{grouptype}"
        while True:
            try:
                # form the name of the next file, then open it
                nextfilename = f"{grouptype}-{fileno}"
                nextfile = open(f"{basedirtemp}\\{nextfilename}.txt", 'r')
                print(f"Reading file {nextfilename}.txt")
                # read each line of the file into a corresponding key of the dictionary using
                # the filename (without extension) as the key and a list of all lines as the value
                datadict[nextfilename] = [line for line in nextfile]
                # increment the value of fileno to match the next file to read
                fileno += 1
                # close the file
                nextfile.close()
            except FileNotFoundError:
                # when we get a filenotfound exception, it would probably mean we have read all the files
                print(f"file {basedirtemp}\\{nextfilename}.txt not found. All files must have been read. If the number"
                      "in the file name in this message is less than 11, a file may have been deleted, "
                      "so check again\nContinuing")
                break
            # end except
        # end while
    # end for
# end def


# this function filters out all dialog from the group of documents except the childs dialog
# Argument #1: a dictionary containing the documents of a given group
def keep_child_dialogs(groupdict):
    # this will temporarily store the filtered set of documents
    temp_dict = groupdict

    # iterate over each key/value pair of the dictionary ie for each document
    for key, document in groupdict.items():
        # reset the temp dict for this key to an empty list
        temp_dict[key] = []
        print(f"Filtering document {key}.txt for *CHI lines:")
        # iterate over each line in the current document
        for lNum, line in enumerate(document):
            # if the first four characters are *CHI, this is a line we want. Now we must check if
            # this dialog spills over to the next line, so we keep n (number of lines to look ahead) as 1
            if line[0:4] == '*CHI':
                # print(f"Found target on line {lNum}: {line}. Checking for overflow:")
                # number of lines to check after this for dialog overflow
                n = 1
                while True:
                    # if the first character of the current line we are checking is the tab (\t), then that means
                    # this is a continuation of the childs dialog. So concatenate this with the original line we
                    # are checking
                    if document[lNum + n][0] == '\t':
                        # print(f"Found an overflow on n = {n}, appending to original line {lNum}. "
                        #       f"Checking for next line overflow:")
                        line += document[lNum + n]
                        n += 1
                    # else, we don't need the next line, so break out of this loop
                    else:
                        # print(f"Overflow not found, moving on")
                        break
                    # end if
                # end while
                temp_dict[key].append(line)
            # end if
        # end for
        print(f"found {len(temp_dict[key])} matches in {key}.txt")
    # end for
    # return the filtered dict we created and filled
    return temp_dict
#  end def


# def filterChats(chatdict):
def filterChats(chatdict: Dict[str, List[str]]):
    tempdict = dict(chatdict)

    # for each file in the dict of files
    for filename, lines in chatdict.items():
        # for each linenum and it's line in the file
        for lineno, line in enumerate(lines):
            # tokenize the line
            linetoks = line.split()
            filteredline = []
            for col, tok in enumerate(linetoks):
                # Perfrom filter (d)
                if tok != "(.)":
                    toklist = list(tok)
                    toklist = [s for s in toklist if s not in "()"]
                    tok = "".join(toklist)
                # perform filter (b)
                strippedtok = tok.strip('<>').replace("<", " ").replace(">", " ")
                if len(strippedtok) > 0 and strippedtok[0] not in '&+':
                    filteredline.append(strippedtok)
                # end if
            # end for
            del col, tok

            # generate a full line string from the list again
            joinedline = " ".join(filteredline)

            start = joinedline.find('[')
            end = joinedline.find(']') + 1
            if start > 0 and end > 0:
                while True:
                    try:
                        interestingtok = joinedline[start: end]
                        if interestingtok not in ['[/]', '[//]', '[* m:+ed]']:
                            joinedline = joinedline[0:start] + joinedline[end:]
                            start -= len(interestingtok)
                            end -= len(interestingtok)
                        # end if
                        start = joinedline.index('[', end + 1)
                        end = joinedline.index(']', end) + 1
                    except ValueError:
                        break
                    # end except
                # end while
            # endif
            lines[lineno] = joinedline
        # end for
        tempdict[filename] = lines
    # end for
    return tempdict
# end def


def main():
    read_files()

    print(tdFileContents.keys())
    print(sliFileContents.keys())

    filteredtdfile = keep_child_dialogs(tdFileContents)
    filteredsdfile = keep_child_dialogs(sliFileContents)

    filteredtdfile = filterChats(filteredtdfile)
    filteredsdfile = filterChats(filteredsdfile)

    # Write to output cleaned destination
    for group in [(groupTD, filteredtdfile), (groupSLI, filteredsdfile)]:
        gname, gdict = group
        for filename, contents in gdict.items():
            ofile = open(f"./cleaned/{gname}_cleaned/{filename}.txt", 'w')
            ofile.write('\n'.join(gdict[filename]))
            ofile.close()
        # end for
    # end def

# end def


if __name__ == "__main__":
    main()
# end if
