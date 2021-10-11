
## dirtree.py
Fabiano Barufaldi (barufa@gmail.com)

Cocus challenge # 1 - File listing

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


#### Definition

Find all files within a path, with a given file name suffix. Note that a path may contain further subdirectories and those subdirectories may also contain further subdirectories. There is no limit
to the depth of the subdirectories.

Arguments:
- suffix(str): suffix if the file name to be found
- path(str): path of the file system

Returns:
- a list of paths and file names that match the suffix

#### Expected deliverable
Your code should be executable with the following call “ yourScript.py *.log /var/tmp”.

See below for an example of what the output should be (for a given scenario):

Scenario:
      |-- a
    | |-- bbb
    | |-- bbb.log
    | |-- ddd
    |-- aaa.log
    |-- abc.txt

Output:
./aaa.log
./a/bbb.log

### Running
```
python3 -m pip install -r requirements.txt

chmod +x dirtree.py

usage: dirtree.py [-h] target_directory filename_pattern

positional arguments:
  target_directory  target directory
  filename_pattern  file pattern (between quotes)

optional arguments:
  -h, --help        show this help message and exit

```
