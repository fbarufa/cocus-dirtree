#!/usr/bin/python3
# dirtree.py
# Fabiano Barufaldi - barufa@gmail.com - 2021-10-10.
# Cocus challenge #1 - File listing

import os
import fnmatch
import argparse
from collections import defaultdict


def find_matching_files(directory, file_pattern):

    # directory could be a relative path, so transform it into an absolute path
    directory = os.path.abspath(directory)
    directory_to_matched_files = defaultdict(list)

    # walk directories, files searching for matches
    for root, _, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file.lower(), file_pattern):
                directory_to_matched_files[root].append(file)

    return directory_to_matched_files


if __name__ == '__main__':

    # command line argument parser
    parser = argparse.ArgumentParser()

    parser.add_argument("target_directory", help="target directory", type=str)
    parser.add_argument("filename_pattern",
                        help="file pattern (between quotes)", type=str)

    args = parser.parse_args()

    # initial screen
    # os.system('cls||clear')

    print("** DIRTREE - looking for file pattern '" +
          args.filename_pattern.lower() +
          "' at " + args.target_directory)

    # find files in directory according to file pattern
    files = find_matching_files(args.target_directory,
                                args.filename_pattern.lower())

    # list files (or not)
    file_count = 0
    if len(files.keys()) > 0:

        # iterate directories / files
        for dir in files.keys():
            for file in files[dir]:

                # convert to relative path
                dir = dir.replace(args.target_directory, ".")

                # list matching entry
                print(dir + '/' + file)
                file_count += 1

        print('\n', 'Total ' + str(file_count) + ' file(s)')

    else:
        print('\n', 'File pattern not found in directory tree')
