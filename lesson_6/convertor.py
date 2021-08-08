"""
Program that asks for a filename as a input to the user. Given the filename, validates it,
and reads it content in order to convert the meters to feet. The final step is to create a new file with those new
feet measures.
"""

import sys
import os
import csv

NUMBER_OF_ARGS = 2
ARG_FILE_NAME = 1
REQUIRED_EXTENSION = 'csv'
METERS_FEET_RATIO = 3.28084


def validate_filename(filename):
    """Given a filename, checks if it is valid."""
    if not filename:
        raise ValueError("The filename cannot be an empty string.")

    split_filename = filename.split('.')

    if split_filename[-1] != REQUIRED_EXTENSION:
        raise TypeError("Invalid extension: the file must be a csv file.")

    if not os.path.exists(filename):
        raise FileNotFoundError(f"The provided file '{filename}' doesn't exist.")


def convert_file(filename):
    """
    Given a valid filename, reads it content, convert each cell (in meters) to feet, creates the new csv file,
    and add those converted meters into it.
    """
    [path, extension] = filename.split('.')
    conversions = []

    with open(filename, 'r') as opened_file:
        csv_reader = csv.reader(opened_file)
        for row in csv_reader:
            validate_row(row)

            meters = float(row[0])
            conversions.append({'meters': meters, 'feet': meters_to_feet(meters)})

    write_converted_values(f"{path}_new.{extension}", conversions)


def validate_row(row):
    """Given the value of the cell, check if it is valid and raise an error if it is not."""
    if len(row) != 1:
        raise ValueError("The row is invalid. It contains more than 1 column.")

    [meters] = row

    # I decided to consider negative values as invalid values
    if meters is None or not meters.isnumeric():
        raise ValueError(f"There is a cell that contains an invalid value ({meters}). It should be a positive number.")


def meters_to_feet(meters):
    """Converts meters to feet."""
    return meters * METERS_FEET_RATIO


def write_converted_values(new_filename, conversions):
    """Given the new filename and the conversions, tries to write each converted row into a new file."""

    if len(conversions) == 0:
        raise ValueError("The file doesn't have any row with values.")
    else:
        new_opened_file = open(new_filename, 'w+')
        fieldnames = conversions[0].keys()
        csv_writer = csv.DictWriter(new_opened_file, fieldnames=fieldnames)
        csv_writer.writerows(conversions)
        new_opened_file.close()


def main():
    """
    Gets user input - file name
    Reads text file, converts every cell in the csv file from meters to feet
    """

    if len(sys.argv) != NUMBER_OF_ARGS:
        print("usage: ./convertor.py /path/to/file")
        sys.exit(1)

    filename = sys.argv[ARG_FILE_NAME]

    try:
        validate_filename(filename)
        convert_file(filename)
    except ValueError as e:
        print(f"ValueError - {e}")
    except TypeError as e:
        print(f"TypeError - {e}")
    except FileNotFoundError as e:
        print(f"FileNotFoundError - {e}")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
