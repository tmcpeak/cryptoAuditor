cryptoAuditor<br>
=============<br>

A simple Python script to find crypto usages in Python source<br>


Put the names of crypto libraries (one per line) under the [libs] section.  Entries are case-insensitive.
Libraries names will only be checked in lines which contain "import".<br>

Functions can be listed (one per line) under the [funcs] section.  Entries are case-insensitive.  Functions are checked in any lines.<br>


Usage:<br>
python AuditCrypto.py -l CryptoDict.txt -d <codePath><br><br>
-l optional argument to specify the list of crypto libaries and functions to scan for.  If not specified will use CryptoDict.txt from the current directory.<br>
-d optional argument to specify the directory of code to scan.  If not specified will use './'<br><br>


TODO:<br>
  1) Build the dictionary file with more crypto libraries and functions<br>
  2) Better output of the results (file: HTML?)<br>
  3) Exception handling when dictionary file or code directory do not exist<br>




