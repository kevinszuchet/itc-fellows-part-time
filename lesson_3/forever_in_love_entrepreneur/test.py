from ex7 import FileManager
import io
import unittest.mock
import os
from pathlib import Path
import hashlib
import shutil


class Testing(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.test_write('Hello World', "test.txt")
        self.test_read('Hello World', "test_02.txt")
        self.test_append('Hello', ' World!', "test_02.txt")
        help_msg = ("File Manager commands:\n"
                    "read <text_file>            : print the text within <text_file>.\n"
                    "write '<text>' <output_file>: replace everything to <text> in <output_file>.\n"
                    "append '<text>' <file_path> : append <text> into <file_path>.\n"
                    "list_dir <dir> <extension>  : list all files in <dir>.\n"
                    "exists <file>               : check if <file> exists in this directory and nested directory.\n"
                    "md5 <file>                  : returns md5 result on the contents of <file>.\n"
                    "exit                        : exit the file manager program.\n")
        help_msg += "\n"
        self.test_print_help(help_msg)
        self.test_exists("not_existent_file.txt")
        self.test_md5("not_existent_file.txt", "Hello World")
        self.test_list_dir("./something")
        print('All tests passed')

    @staticmethod
    def test_write(string, file_name):
        FileManager.write(string, file_name)
        with open(file_name) as file:
            data = file.read()
            assert data == string, 'Testing write to file'
        os.remove(file_name)
        print('test_write passed')

    @staticmethod
    def test_append(original_string, concat_string, file_name):
        with open(file_name, "w+") as file:
            file.write(original_string)
        FileManager.append(concat_string, file_name)
        with open(file_name, "r") as file:
            data = file.read()
            assert data == original_string + concat_string, 'Testing appending to file'
        os.remove(file_name)
        print('test_append passed')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_read(self, string, file_name, mock_stdout):
        """"Testing for read(text.txt)"""
        with open(file_name, "w+") as file:
            file.write(string)
        FileManager.read(file_name)
        expected_output = f"File content:\n{string}\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output), "Testing read file"
        os.remove(file_name)
        print('test_read passed')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_help(self, string, mock_stdout):
        """"Testing for read(text.txt)"""
        FileManager.print_help()
        self.assertEqual(mock_stdout.getvalue(), string), "Testing Print help"
        print('test_print_help passed')

    def test_exists(self, file_path):
        self.test_exists_existing_file(file_path)
        self.test_exists_not_existing_file(file_path)
        print('test_exists passed')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_exists_existing_file(self, file_path, mock_stdout):
        if not Path(file_path).exists():
            open(file_path, "w").close()
        FileManager.exists(file_path)
        expected_output = f"File {file_path} exists"
        expected_output += "\n"
        os.remove(file_path)
        self.assertEqual(mock_stdout.getvalue(), expected_output), "Testing reading existing file"

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_exists_not_existing_file(self, file_path, mock_stdout):
        # creating the file
        while Path(file_path).exists():
            file_path = "_" + file_path
        open(file_path, "w").close()
        FileManager.exists(file_path)
        expected_output = f"File {file_path} exists"
        expected_output += "\n"
        os.remove(file_path)
        self.assertEqual(mock_stdout.getvalue(), expected_output), "Testing reading existing file"
        print('test_exists_not_existing_file passed')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_md5(self, file_path, content, mock_stdout):
        while Path(file_path).exists():
            file_path = "_" + file_path
        with open(file_path, "w") as f:
            f.write(content)
        text = Path(file_path).read_text()
        result = hashlib.md5(text.encode())
        expected_output = "MD5 result:" + "\n" + str(result.digest()) + "\n"
        FileManager.md5(file_path)
        self.assertEqual(mock_stdout.getvalue(), expected_output), "Testing md5"
        os.remove(file_path)
        print('test_md5 passed')

    def test_list_dir(self, folder_path):
        self.test_list_dir_existing_file(folder_path)
        self.test_list_dir_empty_dir(folder_path)
        self.test_list_dir_with_extension(folder_path)
        self.test_list_dir_with_extension_no_files(folder_path)
        self.test_list_dir_not_existing_folder(folder_path)
        print('test_list_dir passed')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_dir_existing_file(self, dir_folder, mock_stdout):
        folder_path = Path(dir_folder)
        if folder_path.is_dir():
            raise ValueError('Test directory should not exist')
        folder_path.mkdir(parents=True, exist_ok=True)
        open(folder_path.joinpath('test.txt'), "w").close()
        open(folder_path.joinpath('_test.txt'), "w").close()
        FileManager.list_dir(dir_folder)
        shutil.rmtree(folder_path)
        expected_output = f"_test.txt\n"
        expected_output += f"test.txt\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output), "Testing list dir"

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_dir_empty_dir(self, dir_folder, mock_stdout):
        folder_path = Path(dir_folder)
        if folder_path.is_dir():
            raise ValueError('Test directory should not exist')
        folder_path.mkdir(parents=True, exist_ok=True)
        FileManager.list_dir(dir_folder)
        shutil.rmtree(folder_path)
        expected_output = f"No files in folder\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output), "Testing list dir"

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_dir_with_extension(self, dir_folder, mock_stdout):
        folder_path = Path(dir_folder)
        if folder_path.is_dir():
            raise ValueError('Test directory should not exist')
        folder_path.mkdir(parents=True, exist_ok=True)
        open(folder_path.joinpath('test.txt'), "w").close()
        open(folder_path.joinpath('_test.jpg'), "w").close()
        FileManager.list_dir(dir_folder, ".jpg")
        shutil.rmtree(folder_path)
        expected_output = f"_test.jpg\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output), "Testing list dir"

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_dir_with_extension_no_files(self, dir_folder, mock_stdout):
        folder_path = Path(dir_folder)
        if folder_path.is_dir():
            raise ValueError('Test directory should not exist')
        folder_path.mkdir(parents=True, exist_ok=True)
        open(folder_path.joinpath('test.txt'), "w").close()
        open(folder_path.joinpath('_test.txt'), "w").close()
        FileManager.list_dir(dir_folder, ".jpg")
        shutil.rmtree(folder_path)
        expected_output = f"No files in folder with the given extension\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output), "Testing list dir"

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_dir_not_existing_folder(self, dir_folder, mock_stdout):
        folder_path = Path(dir_folder)
        if folder_path.is_dir():
            raise ValueError('Test directory should not exist')
        FileManager.list_dir(dir_folder, ".jpg")
        expected_output = f"Provided path is not a directory\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output), "Testing list dir"


if __name__ == '__main__':
    Testing()
