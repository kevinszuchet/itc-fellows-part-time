import hashlib
from pathlib import Path
import argparse
import shutil
import pyAesCrypt
from zipfile import ZipFile


class FileManager(dict):
    def __init__(self):
        super().__init__()
        self.help = {
            "read": "read <text_file>: print the text within <text_file>.\n",
            "write": "write '<text>' <output_file>: replace everything to <text> in <output_file>.\n",
            "append": "append '<text>' <file_path>: append <text> into <file_path>.\n",
            "list_dir": "list_dir <dir> <extension>: list all files in <dir>.\n",
            "exists": "exists <file>: check if <file> exists in this directory and nested directory.\n",
            "md5": "md5 <file>: returns md5 result on the contents of <file>.\n",
            "exit": "exit: exit the file manager program.\n",
            "move": "moves the file from <source_file> to <dest>.\n",
            "copy": "copies the file from <source_file> to <dest>.\n",
            "mkdir": "creates <dir>.\n",
            "rmdir": "removes <dir>, and all of its contents.\n",
            "zip": "creates a zipped version of <source_file>.\n",
            "encrypt": "encrypt <file> using AES, and <password> as its key.\n",
            "decrypt": "decrypt <file> using AES, and <password> as its key.\n"
        }
        self.map = {
            "read": {
                "method": self.read,
                "help_msg": self.help['read'],
                "params": [{
                    "name": "text_file",
                    "positional": True,
                    "type": str,
                    "help": "Path string to a file"
                }]
            },
            "write": {
                "method": self.write,
                "help_msg": self.help['write'],
                "params": [
                    {
                        "name": "text",
                        "positional": True,
                        "type": str,
                        "help": "String to write"
                    },
                    {
                        "name": "output_file",
                        "positional": True,
                        "type": str,
                        "help": "Output file"
                    },
                ]
            },
            "append": {
                "method": self.append,
                "help_msg": self.help['append'],
                "params": [
                    {
                        "name": "text",
                        "positional": True,
                        "type": str,
                        "help": "String to append"
                    },
                    {
                        "name": "file_path",
                        "positional": True,
                        "type": str,
                        "help": "File to append to"
                    }
                ]
            },
            "list_dir": {
                "method": self.list_dir,
                "help_msg": self.help['list_dir'],
                "params": [
                    {
                        "name": "dir",
                        "positional": True,
                        "type": str,
                        "help": "Path to a directory"
                    },
                    {
                        "name": "extension",
                        "positional": False,
                        "type": str,
                        "help": "Extension to use as filter"
                    }
                ]
            },
            "exists": {
                "method": self.exists,
                "help_msg": self.help['exists'],
                "params": [
                    {
                        "name": "file",
                        "positional": True,
                        "type": str,
                        "help": "Path string to a file"
                    }
                ]
            },
            "md5": {
                "method": self.md5,
                "help_msg": self.help['md5'],
                "params": [
                    {
                        "name": "file",
                        "positional": True,
                        "type": str,
                        "help": "Path string to a file"
                    }
                ]
            },
            "move": {
                "method": self.move,
                "help_msg": self.help['move'],
                "params": [
                    {
                        "name": "source_file",
                        "positional": True,
                        "type": str,
                        "help": "Path string to a file"
                    },
                    {
                        "name": "dest",
                        "positional": True,
                        "type": str,
                        "help": "destination path to move. If it is a filename, it renames too. "
                    }
                ]
            },
            "copy": {
                "method": self.copy,
                "help_msg": self.help['copy'],
                "params": [
                    {
                        "name": "source_file",
                        "positional": True,
                        "type": str,
                        "help": "Path string to a file"
                    },
                    {
                        "name": "dest",
                        "positional": True,
                        "type": str,
                        "help": "destination path to copy. If it is a filename, it renames too. "
                    }
                ]
            },
            "mkdir": {
                "method": self.mkdir,
                "help_msg": self.help['mkdir'],
                "params": [
                    {
                        "name": "dir",
                        "positional": True,
                        "type": str,
                        "help": "dir to be created"
                    }
                ]
            },
            "rmdir": {
                "method": self.rmdir,
                "help_msg": self.help['rmdir'],
                "params": [
                    {
                        "name": "dir",
                        "positional": True,
                        "type": str,
                        "help": "dir to be removed"
                    }
                ]
            },
            "zip": {
                "method": self.zip,
                "help_msg": self.help['zip'],
                "params": [
                    {
                        "name": "source_file",
                        "positional": True,
                        "type": str,
                        "help": "file to be zipped"
                    },
                    {
                        "name": "zipped_file",
                        "positional": False,
                        "type": str,
                        "help": "new name to the zipped file"
                    }
                ]
            },
            "encrypt": {
                "method": self.encrypt,
                "help_msg": self.help['encrypt'],
                "params": [
                    {
                        "name": "file",
                        "positional": True,
                        "type": str,
                        "help": "file to encrypt"
                    },
                    {
                        "name": "password",
                        "positional": True,
                        "type": str,
                        "help": "key to encrypt"
                    }
                ]
            },
            "decrypt": {
                "method": self.decrypt,
                "help_msg": self.help['decrypt'],
                "params": [
                    {
                        "name": "file",
                        "positional": True,
                        "type": str,
                        "help": "file to encrypt"
                    },
                    {
                        "name": "password",
                        "positional": True,
                        "type": str,
                        "help": "key to encrypt"
                    }
                ]
            },
        }
        self.main()

    @staticmethod
    def read(text_file):
        """Read text file and print the text to the screen."""
        file_path = Path(text_file)
        return f"File content:\n{file_path.read_text()}"

    @staticmethod
    def write(text, output_file):
        """Write the 'text' to output_file"""
        file_path = Path(output_file)
        file_path.write_text(text)
        return 'Written successfully'

    @staticmethod
    def append(text, file_path):
        """Append 'text' to file_path"""
        path_file = Path(file_path)
        if not path_file.is_file():
            raise FileNotFoundError("File doesn't exist")
        file = Path(file_path).open('a')
        file.write(text)
        file.close()
        return 'Appended successfully'

    @staticmethod
    def list_dir(dir, extension=None):
        """List all file in directory, if extension(.txt) stated, only the file .txt will be printed."""

        # Add '.' into extension if no '.' in extension.
        if extension:
            if extension[0] != '.':
                extension = "." + extension
        folder_path = Path(dir)
        if not folder_path.is_dir():
            return 'Provided path is not a directory'
        if not extension:
            files = [x for x in folder_path.iterdir() if x.is_file()]
        else:
            files = [x for x in folder_path.iterdir() if x.is_file() and x.suffix == extension]
        if not files:
            if not extension:
                return 'No files in folder'
            else:
                return 'No files in folder with the given extension'
        else:
            print_statement = ""
            for file in files:
                print_statement += str(file.name) + '\n'
            return print_statement[:-1]

    @staticmethod
    def exists(file):
        """Check if the file exits."""
        file_path = Path(file)
        if file_path.exists():
            return f"File {file_path.name} exists"
        else:
            return f"File {file_path.name} doesn't exist"

    @staticmethod
    def md5(file):
        """Return md5 result on the contents of file."""
        file_path = Path(file)
        text = file_path.read_text()

        # Encode text to byte to be accepted by md5.
        result = hashlib.md5(text.encode())
        return f"md5 result: {result.digest()}"

    @staticmethod
    def move(source_file, dest):
        """Moves a file from a source to a destination"""
        source_path = Path(source_file)
        dest_path = Path(dest)
        if not source_path.is_file():
            raise FileNotFoundError('source_file should be a file')

        # destination is a folder
        if not dest_path.suffix:
            dest_path.mkdir(parents=True, exist_ok=True)
            shutil.move(source_path.resolve(), dest_path.resolve())
        # destination is a file with wrong extension
        elif dest_path.suffix != source_path.suffix:
            raise OSError('dest should have the same suffix as source_file')
        # destination is a file with the right extension
        else:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(source_path.resolve(), dest_path)
        return 'File moved successfully'

    @staticmethod
    def copy(source_file, dest):
        """Copies a file from a source to a destination"""
        source_path = Path(source_file)
        dest_path = Path(dest)
        if not source_path.is_file():
            raise FileNotFoundError('source_file should be a file')

        # destination is a folder
        if not dest_path.suffix:
            dest_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(source_path.resolve(), dest_path.resolve())

        # destination is a file with wrong extension
        elif dest_path.suffix != source_path.suffix:
            raise OSError('dest should have the same suffix as source_file')

        # destination is a file with the right extension
        else:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(source_path.resolve(), dest_path)
        return 'File copied successfully'

    @staticmethod
    def mkdir(dir):
        """Creates a directory"""
        folder_path = Path(dir)
        if folder_path.exists():
            return 'dir already exists'
        folder_path.mkdir(parents=True, exist_ok=True)
        return f'dir created successfully'

    @staticmethod
    def rmdir(dir):
        """Removes a directory"""
        folder_path = Path(dir)
        if not folder_path.exists():
            return "dir doesn't exist"
        shutil.rmtree(dir)
        return "dir removed successfully"

    @staticmethod
    def zip(source_file, zipped_file=None):
        """Zips a file"""
        source_path = Path(source_file)
        if not source_path.is_file():
            return 'source_file should be a file'
        if not zipped_file:
            new_path = source_path.with_suffix('.zip')
        else:
            new_path = source_path.with_stem(zipped_file).with_suffix('.zip')
        with ZipFile(new_path.absolute(), 'w') as myzip:
            myzip.write(source_path)
        return "Zipped successfully"

    @staticmethod
    def encrypt(file, password):
        """Ecnrypts a file"""
        file_path = Path(file)
        if not file_path.is_file():
            raise FileNotFoundError('file should exist')
        if not password:
            raise ValueError('Password should be valid')
        new_name = file_path.with_stem(file_path.name).with_suffix('.aes')
        pyAesCrypt.encryptFile(file_path.resolve(), new_name, password)
        return 'Encrypted Successfully'

    @staticmethod
    def decrypt(file, password):
        """Decrypts a file"""
        file_path = Path(file)
        if not file_path.is_file():
            raise FileNotFoundError('file should exist')
        if not file_path.suffix == '.aes':
            raise FileNotFoundError('file should have .aes extension')
        new_name = file_path.with_name(file_path.stem)
        pyAesCrypt.decryptFile(file_path.resolve(), new_name, password)
        return 'Decrypted Successfully'

    def main(self):
        """Launches the file manager"""
        parser = argparse.ArgumentParser()
        sub_parser = parser.add_subparsers(dest="command")
        for action in self.map:
            nested_parser = sub_parser.add_parser(action, help=self.map[action]['help_msg'])
            for subcommand in self.map[action]['params']:
                if subcommand['positional']:
                    nested_parser.add_argument(subcommand['name'], type=subcommand['type'],
                                               help=subcommand['help'])
                else:
                    nested_parser.add_argument("--" + subcommand['name'], type=subcommand['type'],
                                               help=subcommand['help'])
        args = parser.parse_args()
        inputs = vars(args)
        command = inputs['command']
        inputs.pop('command')
        try:
            result = self.map[command]['method'](**inputs)
            print(result)
        except (FileNotFoundError, OSError, TypeError, ValueError) as e:
            print('An error occurred:')
            print(f"\t{e}")
        except KeyError:
            print('An error occurred:')
            print(f"\tPlease provide one command at least. Refer to help for further assistance")


def main():
    FileManager()


if __name__ == '__main__':
    main()
