cryptoAuditor
=============

A simple Python script to find crypto usages in Python source


Put the names of crypto libraries (one per line) under the [libs] section.  Entries are case-insensitive.
Libraries names will only be checked in lines which contain "import".   

Functions can be listed (one per line) under the [funcs] section.  Entries are case-insensitive.  Functions are checked in any lines.





TODO:
  1) Build the dictionary file with more crypto libraries and functions
  2) Allow the directory and file to be specified on the command line
  3) Better output of the results (file: HTML?)




