from argparse import ArgumentParser
import sys
import os
import re
from pathlib import Path
    
# i have zero clue how to code properly, i fear
def main(filename, file_to_write_to, o, n, r):
    regex_patterns = ""
    if r:
        for regex in r:
            regex_patterns = regex_patterns + f"{regex}|"
    regex_patterns = rf"{regex_patterns}"
        
    if Path(file_to_write_to).is_file() and (o == "Yes"):
        os.remove(file_to_write_to)
        
    string_list = ["[INTERVIEWER]", "[PARTICIPANT]"]
    if n:
        string_list = [names for names in n]
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [re.sub(regex_patterns, "", line.rstrip("\n")) for line in file.readlines()]
    lastone = "a"
    
    lines_2 = []
    for l in lines:
        if l:
            lines_2.append(l)
    #print(lines_2)
    
    lines_3 = []
    for l in lines_2:
        l = l.strip()
        if not lastone == l:
            if l in string_list:
                lines_3.append("\n" + "\n"+ l + " ")
            else:
                lines_3.append(l + " ")
        if l in string_list:
            lastone = l.strip()
        
        #print(lastone)
    
    lines_3[0] = lines_3[0].replace("\n", "")
    with open(file_to_write_to, "a") as file:
        for item in lines_3:
            file.write(f"{item}")
    
    
def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file", help="path to energy CSV file")
    parser.add_argument("file_to_write_to", help = "file to write to")
    parser.add_argument("-o", default = "No", help = "before running, delete file to write to?")
    parser.add_argument("-n", nargs = "*", help = "names to filter by. defaults to [INTERVIEWER] and [PARTICIPANT] otherwise. ")
    parser.add_argument("-r", nargs = "*", help = "regex patterns to remove from file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file, args.file_to_write_to, args.o, args.n, args.r)
