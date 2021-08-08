"""Command-line program that receives a name of a command and possible additional arguments to exec it."""

import argparse
import os
import sys

COMMANDS = ["read", "write", "append", "list_dir", "exists", "md5", "move", "copy", "mkdir", "rmdir", "zip",
            "encrypt", "decrypt"]


def read_parser():
    """It creates the read parser."""
    parser = argparse.ArgumentParser(prog="read", description="print the text from within <text_file> to the screen")
    parser.add_argument("text_file", metavar="<text-file>", type=str, help="the path to the file")
    # args = parser.parse_args()
    # read_file(args.text_file)


def write_parser():
    """It creates the write parser."""
    parser = argparse.ArgumentParser(prog="write", description="write the <text> into <output_file>")
    parser.add_argument("text", metavar="<text>", type=str, help="text to write")
    parser.add_argument("output_file", metavar="<output-file>", type=str, help="the path to the destination")
    # args = parser.parse_args()
    # write_file(args.text, args.output_file)


def append_parser():
    """It creates the append parser."""
    parser = argparse.ArgumentParser(prog="append", description="append the <text> into <file_path>")
    parser.add_argument("text", metavar="<text>", type=str, help="text to append")
    parser.add_argument("file_path", metavar="<file_path>", type=str, help="the path to the file")


def list_dir_parser():
    """It creates the list_dir parser."""
    parser = argparse.ArgumentParser(prog="list_dir", description="list all files in <dir>")
    parser.add_argument("dir", metavar="<dir>", type=str, help="dir with files to list")
    parser.add_argument("extension", metavar="[extension]", type=str,
                       help="Optional extension to filter files to list in <dir>")


def exists_parser():
    """It creates the exists parser."""
    parser = argparse.ArgumentParser(prog="exists", description="checks if <file> exists")
    parser.add_argument("file", metavar="<file>", type=str, help="the path to the file")


def md5_parser():
    """It creates md5 read parser."""
    parser = argparse.ArgumentParser(prog="md5", description="returns the md5 result on the contents of <file>")
    parser.add_argument("file", metavar="<file>", type=str, help="the path to the file")


def move_parser():
    """It creates move read parser."""
    parser = argparse.ArgumentParser(prog="move", description="moves the file from <source_file> to <dest>")
    parser.add_argument("source_file", metavar="<source_file>", type=str, help="the path to the file")
    parser.add_argument("dest", metavar="<dest>", type=str,
                       help="""if <dest> specifiies a filename – it should be the new file name for <source_file> 
                            if <dest> specifies a directory – the original filename should be preserved""")


def copy_parser():
    """It creates copy read parser."""
    parser = argparse.ArgumentParser(prog="copy", description="copies the file from <source_file> to <dest>")
    parser.add_argument("source_file", metavar="<source_file>", type=str, help="the path to the file")
    parser.add_argument("dest", metavar="<dest>", type=str,
                       help="""if <dest> specifiies a filename – it should be the new file name for <source_file> 
                            if <dest> specifies a directory – the original filename should be preserved""")


def mkdir_parser():
    """It creates the mkdir parser."""
    parser = argparse.ArgumentParser(prog="mkdir", description="creates <dir>")
    parser.add_argument("dir", metavar="<dir>", type=str, help="the path to the dir")


def rmdir_parser():
    """It creates the rmdir parser."""
    parser = argparse.ArgumentParser(prog="rmdir", description="removes <dir>, and all of its contents")
    parser.add_argument("dir", metavar="<dir>", type=str, help="the path to the dir")


def zip_parser():
    """It creates zip read parser."""
    parser = argparse.ArgumentParser(prog="zip",
                                    description="creates a zipped version of <source_file> in the same directory")
    parser.add_argument("source_file", metavar="<source_file>", type=str, help="the path to the source file")
    parser.add_argument("zipped_file", metavar="[zipped_file]", type=str,
                       help="Optional path to create the compressed file as [zipped_file]")


def aes_parser(command):
    """It creates the aes encryption/decryption parser. It depends on the command argument."""
    parser = argparse.ArgumentParser(prog=command, description=f"{command} <file> using AES, and <password> as its key")
    parser.add_argument("file", metavar="<file>", type=str, help="the path to the file")
    parser.add_argument("password", metavar="<password>", type=str, help="password for AES key")

    return aes_parser


encrypt_parser = aes_parser("encrypt")  # Function that creates the encrypt parser parser
decrypt_parser = aes_parser("decrypt")  # Function that creates the decrypt parser parser


def read(filename):
    """Given a filename, tries to read a file and prints its text."""
    print("filename", filename)
    try:
        text_file = open(filename, mode="r")
        text = text_file.read()
        text_file.close()
        print(text)
    except FileNotFoundError:
        print(f"The filename {filename} wasn't found.")


def write(text, output_filename):
    """Given a filename, tries to read a file and prints its text."""
    if not os.path.exists(output_filename):
        os.makedirs(output_filename)

    output_file = open(output_filename, mode="w")
    output_file.write(text)


def append(): pass


def list_dir(): pass


def exists(): pass


def md5(): pass


def move(): pass


def copy(): pass


def mkdir(): pass


def rmdir(): pass


def zip(): pass


def encrypt(): pass


def decrypt(): pass


def add_parsers():
    """Given a parser, adds the parsers in order to create all the commands with their arguments."""
    [eval(command + "_parser")() for command in COMMANDS]


def main():
    """Main function. It creates the Argument Parser and calls some functions in order to configure it."""
    add_parsers()


if __name__ == "__main__":
    """Calls the main function."""
    main()
