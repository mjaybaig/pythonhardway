# cat.py: a 45 minute challenge to implement as much of the cat linux command as possible
# Author: M Jameel Baig
import sys
import argparse

def main():
    # args = sys.argv[1:]

    textcontent = []
    # for filename in args:
    #     filetext = ""
    #     filehandle = open(filename)
    #     filetext = [line for line in filehandle]
    #     textcontent += filetext
    #     filehandle.close()

    # print(textcontent)
    # print("\n".join(textcontent))

    # using argparse

    parser = argparse.ArgumentParser(description="concatenate the files")
    parser.add_argument('files', nargs='+')   

    args = parser.parse_args()
    # print(args.files)

    for filename in args.files:
        filetext = ""
        filehandle = open(filename)
        filetext = filehandle.readlines()
        textcontent.append("".join(filetext))
        filehandle.close()
    # end for
    # print(args)
    print("\n\n".join(textcontent))
    print(textcontent)
if __name__ == "__main__":
    main()