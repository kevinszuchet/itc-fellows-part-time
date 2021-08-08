import re
import hashlib
from pathlib import Path


class FileManager:
    def __init__(self):
        self.main()

    @staticmethod
    def read(text_file):
        """Read text file and print the text to the screen."""
        file_path = Path(text_file)
        print('File content:')
        print(file_path.read_text())

    @staticmethod
    def write(text, output_file):
        """Write the 'text' to output_file"""
        file_path = Path(output_file)
        file_path.write_text(text)
        print('Written successfully')

    @staticmethod
    def append(text, file_path):
        """Append 'text' to file_path"""
        file = Path(file_path).open('a')
        file.write(text)
        file.close()
        print('Appended successfully')

    @staticmethod
    def list_dir(dir_path, extension=None):
        """List all file in directory, if extension(.txt) stated, only the file .txt will be printed."""

        # Add '.' into extension if no '.' in extension.
        if extension:
            if extension[0] != '.':
                extension = "." + extension
        folder_path = Path(dir_path)
        if not folder_path.is_dir():
            print('Provided path is not a directory')
            return
        if not extension:
            files = [x for x in folder_path.iterdir() if x.is_file()]
        else:
            files = [x for x in folder_path.iterdir() if x.is_file() and x.suffix == extension]
        if not files:
            if not extension:
                print('No files in folder')
            else:
                print('No files in folder with the given extension')
        else:
            for file in files:
                print(file.name)
        return

    @staticmethod
    def exists(file):
        """Check if the file exits."""
        file_path = Path(file)
        if file_path.exists():
            print(f"File {file_path.name} exists")
        else:
            print(f"File {file_path.name} doesn't exist")

    @staticmethod
    def md5(file):
        """Return md5 result on the contents of file."""
        file_path = Path(file)
        text = file_path.read_text()

        # Encode text to byte to be accepted by md5.
        result = hashlib.md5(text.encode())
        print("MD5 result:")
        print(result.digest())

    @staticmethod
    def print_help():
        """Print help message for all."""
        help_msg = ("File Manager commands:\n"
                    "read <text_file>            : print the text within <text_file>.\n"
                    "write '<text>' <output_file>: replace everything to <text> in <output_file>.\n"
                    "append '<text>' <file_path> : append <text> into <file_path>.\n"
                    "list_dir <dir> <extension>  : list all files in <dir>.\n"
                    "exists <file>               : check if <file> exists in this directory and nested directory.\n"
                    "md5 <file>                  : returns md5 result on the contents of <file>.\n"
                    "exit                        : exit the file manager program.\n")
        print(help_msg)

    def main(self):
        """The main function."""
        func_dic = {
            "read": self.read,
            "write": self.write,
            "append": self.append,
            "list_dir": self.list_dir,
            "exists": self.exists,
            "md5": self.md5,
            "help": self.print_help,
        }

        commands = []
        while True:
            commands = input(">>>")
            if commands == "exit":
                break
            # Get the text from the input.
            text = None
            text_re = re.search('".*"|\'.*\'', commands)
            param = []
            if text_re:
                text = text_re.group(0)
                # Remove the text from commands.
                commands = commands.replace(text, '')
                # Remove first and last character ("" or '')
                text = text[1:len(text) - 1]
                param.append(text)
            # Split out the function param.
            func_params = commands.split()
            function = func_params[0]
            for i in range(1, len(func_params)):
                param.append(func_params[i])

            # If given commands triggered any error, print help message to support user.
            try:
                func_dic.setdefault(function, self.print_help)(*param)
            except (FileNotFoundError, OSError, TypeError):
                print("Invalid Command, please refer to help message below.")
                self.print_help()


def main():
    FileManager()


if __name__ == '__main__':
    main()
