#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
The program takes one or more directories as its arguments and it can:
- List the absolute paths of the special files in all the directories
- Copy the files to the given directory, creating it if necessary
- Create a zipfile containing the files
(We'll say that a "special" file is one where the name contains the pattern __w__,
where the w is one or more word chars.)
"""


# Write functions and modify main() to call them
def get_special_paths(directories):
    """Given a list of directories, returns the absolute path of the special files inside the directories."""
    try:
        absolute_paths = [absolute_path(directory, filename)
                          for directory in directories for filename in os.listdir(directory) if is_special(filename)]
        check_repeated_special_files(absolute_paths)
    except (FileNotFoundError, NotADirectoryError):
        print(f"There are some invalid directories. Please check that all are valid.")
        sys.exit(1)

    return absolute_paths


def check_repeated_special_files(absolute_paths):
    """Given all the absolute paths, it checks that there aren't repeated filenames in different directories."""
    special_filenames = [os.path.basename(abs_path) for abs_path in absolute_paths]
    repeated_special_filenames = {special_filename for special_filename in special_filenames if
                                  special_filenames.count(special_filename) > 1}

    if repeated_special_filenames:
        print(
            f"The next files: {list(repeated_special_filenames)}, are repeated in different directories. Please, fix it.")
        sys.exit(1)


def absolute_path(directory, filename):
    """Given the directory and the filename, joins both, and returns the absolute path to the file."""
    path = os.path.join(directory, filename)
    return os.path.abspath(path)


def is_special(filename):
    """Given a filename, checks if it is special."""
    return re.match(r'.*__\w+__.*', filename)


def copy_to(directories, to_dir):
    """Given a list of directories and a destination directory, copies all the special files in it."""
    special_paths = get_special_paths(directories)

    if not os.path.exists(to_dir):
        os.makedirs(to_dir)

    for special_file in special_paths:
        print(f"Copying {os.path.basename(special_file)} in {to_dir}...")
        shutil.copy(special_file, to_dir)


def zip_to(directories, to_zip):
    """
    Given a list of directories and a destination directory, creates a zip file with all the special directories.
    Then moves it to the to_zip destination.
    """
    special_paths = get_special_paths(directories)


    try:
        command = f"zip -j {to_zip} {' '.join(special_paths)}"
        print(f"Command I'm going to do: {command}")
        subprocess.check_call(command.split(), stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("Cannot execute the command. Please check that all the arguments are valid.")


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print
        "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print
        "error: must specify one or more dirs"
        sys.exit(1)

    if todir:
        copy_to(args, todir)
    elif tozip:
        zip_to(args, tozip)
    else:
        special_paths = get_special_paths(args)
        print(f"Special files:\n" + '\n'.join(special_paths))


if __name__ == "__main__":
    main()
