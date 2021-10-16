# PBDpars
this tool extract the raw PBD path from EXE and DLL files 
usage: PDBpars.py [-h] [-d] [-f] [-k] [-s] [-r] [-qd] [-qf] [-qk] [-qs] [-qr]

extract PDB path from a directory or a file

optional arguments:
  -h, --help           show this help message and exit
  -d , --directory     extract all PDB path from a directory
  -f , --file          extract PDB path from a file
  -k, --keyword        check for bad keywords
  -s, --ascii          check for non ascii characters
  -r , --recursive     extract all PDB path from a directory recursively
  -qd , --qdirectory   extract all PDB path from a directory. no print to console
  -qf , --qfile        extract PDB path from a file. no print to console
  -qk, --qkeyword      check for bad keywords. no print to console unless there is a bad keywords
  -qs, --qascii        check for non ascii characters. no print to console unless there is a non ascii characters
  -qr , --qrecursive   extract all PDB path from a directory recursively. no print to console
