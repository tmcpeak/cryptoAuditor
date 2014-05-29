cryptoAuditor<br>
=============<br>

A simple Python script to find crypto usages in Python source<br>

To use: create a config file with one or more sections<br><br>

Example config file:<br><br>
[libs]<br>
keywords=crypto, OpenSSL, ssl, hashlib, oauthlib, PassLib<br>
output_file=libs.txt<br>
process_comments=True<br><br>

[funcs]<br>
keywords=md5, sha1, sha256, sha384, sha512<br>
process_comments=False<br><br>

TODO:<br>
  1) Build the dictionary file with more crypto libraries and functions<br>
  2) Exception handling when there is a problem with the output files<br>
  3) Handle multi-line comments<br>
  4) Possibly build functionality for using regex<br><br><br>

Example usage:<br>
python AuditCrypto.py -c cryptoConfig.txt<br>
python AuditCrypto.py -c cryptoConfig.txt -d ./codeBase<br>




