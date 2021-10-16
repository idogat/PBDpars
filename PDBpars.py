import os
import argparse


def dire(directory):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".exe") or filename.endswith(".dll"):
            print(os.path.join(directory, filename))
            orig_filename = (os.path.join(directory, filename))
            find_sig(orig_filename)
            continue
        else:
            continue

def q_dire(directory):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".exe") or filename.endswith(".dll"):
            orig_filename = (os.path.join(directory, filename))
            q_find_sig(orig_filename)
            continue
        else:
            continue

def re_dire(re_directory):
    for subdir, dirs, files in os.walk(re_directory):
        for file in files:
            filename = subdir + os.sep + file
            if filename.endswith(".exe") or filename.endswith(".dll"):
                print(filename)
                find_sig(filename)
                continue
            else:
                continue

def q_re_dire(re_directory):
    for subdir, dirs, files in os.walk(re_directory):
        for file in files:
            filename = subdir + os.sep + file
            if filename.endswith(".exe") or filename.endswith(".dll"):
                q_find_sig(filename)
                continue
            else:
                continue

def find_sig(path):
    lst = []
    count = 0
    with open(path, "rb") as bin_file:
        for line in bin_file: #for line in bin file
            lst.append(line)  # put line in list
            if b"RSDS" in line:
                break
            else:
                count+=1
    PDB=str(lst[count:(count + 1)])
    try:
       start=PDB.index("RSDS")
       end=PDB.index(".pdb")
       global final_PDB
       final_PDB=(f"PDB path: {PDB[start:(end+4)]}")
       print(final_PDB)
       if args.keyword:
           keyword()
       if args.ascii:
           nonascii()
       print("__________________________________________________")
    except:
        try:
            print(f"PDB path: {PDB[start:]}")
            if args.keyword:
                keyword()
            if args.ascii:
                nonascii()
            print("__________________________________________________")
        except:
            print("no PDB signature was found")
            print("__________________________________________________")

def q_find_sig(path):
    lst = []
    count = 0
    with open(path, "rb") as bin_file:
        for line in bin_file: #for line in bin file
            lst.append(line)  # put line in list
            if b"RSDS" in line:
                break
            else:
                count+=1
    PDB=str(lst[count:(count + 1)])
    try:
       start=PDB.index("RSDS")
       end=PDB.index(".pdb")
       global final_PDB
       final_PDB=(f"PDB path: {PDB[start:(end+4)]}")
       if args.keyword:
           q_keyword()
       if args.ascii:
           q_nonascii()
    except:
        try:
            global final_PDB2
            final_PDB2=(f"PDB path: {PDB[start:]}")
            if args.keyword:
                q_keyword()
            if args.ascii:
                q_nonascii()
        except:
            return None

def keyword ():
    wordfind=False
    keywords= ("anti","attack","backdoor","bind","bypass","downloader","dropper","exploit","fake","fuck","hack","hide","hook","inject","install","keylog","payload","shell","sleep","spy","trojan")
    for word in keywords:
        if word in final_PDB:
            print(f"word {word} found!")
            wordfind=True
    if wordfind==False:
        print("no bad keywords were found")

def q_keyword ():
    keywords= ("anti","attack","backdoor","bind","bypass","downloader","dropper","exploit","fake","fuck","hack","hide","hook","inject","install","keylog","payload","shell","sleep","spy","trojan")
    for word in keywords:
        if word in final_PDB:
            try:
                print(final_PDB)
                print(f"word {word} found!")
            except:
                print(final_PDB2)
                print(f"word {word} found!")

def nonascii():
    try:
        for path in final_PDB:
            path.encode("ascii")
        print("ascii characters were found")
    except:
        print("non ascii character found!")

def q_nonascii():
    try:
        for path in final_PDB:
            path.encode("ascii")
        return None
    except:
        try:
            print(final_PDB)
            print("non ascii character found!")
        except:
            print(final_PDB2)
            print("non ascii character found!")


parser=argparse.ArgumentParser(description="extract PDB path from a directory or a file")
parser.add_argument("-d","--directory", help="extract all PDB path from a directory",metavar="",required=False)
parser.add_argument("-f", "--file", help="extract PDB path from a file", metavar="",required=False)
parser.add_argument("-k", "--keyword", help="check for bad keywords",required=False,action="store_true")
parser.add_argument("-s", "--ascii", help="check for non ascii characters",required=False,action="store_true")
parser.add_argument("-r", "--recursive", help="extract all PDB path from a directory recursively ", metavar="",required=False)
parser.add_argument("-qd","--qdirectory", help="extract all PDB path from a directory. no print to console ",metavar="",required=False)
parser.add_argument("-qf", "--qfile", help="extract PDB path from a file. no print to console", metavar="",required=False)
parser.add_argument("-qk", "--qkeyword", help="check for bad keywords. no print to console unless there is a bad keywords",required=False,action="store_true")
parser.add_argument("-qs", "--qascii", help="check for non ascii characters. no print to console unless there is a non ascii characters",required=False,action="store_true")
parser.add_argument("-qr", "--qrecursive", help="extract all PDB path from a directory recursively. no print to console", metavar="",required=False)
args = parser.parse_args()

if __name__ == '__main__':
    if args.directory:
        dire(args.directory)
    elif args.file:
        find_sig(args.file)
    elif args.recursive:
        re_dire(args.recursive)
    elif  args.qdirectory:
        q_dire(args.qdirectory)
    elif args.qfile:
        q_find_sig(args.qfile)
    elif args.qrecursive:
        q_re_dire(args.qrecursive)


