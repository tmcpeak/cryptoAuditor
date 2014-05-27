cryptoAuditor
=============

A simple Python script to find crypto usages in Python source


Put the names of crypto libraries (one per line) under the [libs] section.  Entries are case-insensitive.
Libraries names will only be checked in lines which contain "import".   

Functions can be listed (one per line) under the [funcs] section.  Entries are case-insensitive.  Functions are checked in any lines.


Usage:
python AuditCrypto.py -l CryptoDict.txt -d <codePath>
   -l optional argument to specify the list of crypto libaries and functions to scan for.  If not specified will
          use CryptoDict.txt from the current directory.
   -d optional argument to specify the directory of code to scan.  If not specified will use './'


TODO:
  1) Build the dictionary file with more crypto libraries and functions
  2) Better output of the results (file: HTML?)
  3) Exception handling when dictionary file or code directory do not exist




