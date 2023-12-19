# EcoInnovators Backend

## Firebase connection script usage:
```
python firebaseConnection.py [-h] [remote_name] [local_name] (-f | -u | -d)

Firebase connectivity handler

positional arguments:
  remote_name   Remote Data Name
  local_name    Local File name

options:
  -h, --help    show this help message and exit
  -f, --first   Insert data for the first time
  -u, --update  Insert data to remote as append
  -d, --dump    Dump data from remote to local csv
```
