"""Program that given a path to a file, copies it to the destination folder (also given by parameter)."""


def copaste(source, destination):
    """Receives a path to a file, copies it to a given folder."""

    new_destination = get_full_destination(source, destination)
    # Should I have to differentiate between binary files (rb mode) and text files (r mode)?
    source_file, new_destination_file = open_files((source, 'rb'), (new_destination, 'wb'))

    new_destination_file.write(source_file.read())

    close_files(source_file, new_destination_file)


def open_files(*files_with_mode):
    """Receives a list of files with their opening mode, returns the opened files as a tuple."""
    opened_files = []
    for file, mode in files_with_mode:
        opened_files.append(open(file, mode))
    return tuple(opened_files)


def close_files(*files):
    """Given a list of files, closes all of them."""
    opened_files = []
    for file in files:
        file.close()


def get_full_destination(source, destination):
    """Takes a path to a file, finds the file name, returns the new full destination path."""
    split_source = source.split('/')
    file_name = split_source[-1]

    return (destination if destination.endswith('/') else destination + "/") + file_name


def main():
    """"Main function that checks some use cases."""
    """
    The use cases are attached to my computer. That is the reason why I commented on them.
    copaste(r"/home/kevinszuchet/Downloads/dni.jpg", r"/home/kevinszuchet/PycharmProjects/lesson_3")
    copaste(r"/home/kevinszuchet/Downloads/ITC for MASA - program list.pdf",
            r"/home/kevinszuchet/PycharmProjects/lesson_3")
    copaste(r"/home/kevinszuchet/Downloads/png2jpg.zip", r"/home/kevinszuchet/PycharmProjects/lesson_3")
    copaste(r"/home/kevinszuchet/Downloads/file.txt", r"/home/kevinszuchet/PycharmProjects/lesson_3")
    """
    copaste(r"/home/kevinszuchet/Downloads/dni.jpg", r"/home/kevinszuchet/PycharmProjects/lesson_3")
    copaste(r"/home/kevinszuchet/Downloads/ITC for MASA - program list.pdf",
            r"/home/kevinszuchet/PycharmProjects/lesson_3")
    copaste(r"/home/kevinszuchet/Downloads/png2jpg.zip", r"/home/kevinszuchet/PycharmProjects/lesson_3")
    copaste(r"/home/kevinszuchet/Downloads/file.txt", r"/home/kevinszuchet/PycharmProjects/lesson_3")


if __name__ == "__main__":
    main()
