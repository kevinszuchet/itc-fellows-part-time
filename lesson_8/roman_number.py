# Module imports
import re

# Global parameters
ROMAN_NUMBERS_TABLE = [
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100), ("XC", 90),
    ("L", 50), ("XL", 40), ("X", 10),
    ("IX", 9), ("V", 5), ("IV", 4),
    ("I", 1)
]

ROMAN_NUMBERS_DICT = {key: value for key, value in ROMAN_NUMBERS_TABLE}


class RomanNumber:

    def __init__(self, string):
        """
        Initialize the roman number
        :param string: roman number in a string
        """

        if not self.is_valid(string):
            print("not valid", string)
            raise ValueError(f"Invalid roman number: {string}")

        self._roman = string
        self._arab = self.to_arab()

    def __add__(self, other):
        """
        Add a number (roman or not), to a roman number
        :param other: an integer / roman number
        :return: a roman number with the sum of the two numbers
        """
        other_number = self._try_to_get_the_other_number(other)
        return RomanNumber.to_roman(self.to_arab() + other_number)

    def __radd__(self, other):
        """
        Add roman number, to another  number (roman or not)
        :param other: an integer / roman number
        :return: a roman number with the sum of the two numbers
        """
        return self + other

    def __sub__(self, other):
        """
        Subtract a number (roman or not), from a roman number
        :param other: an integer / roman number
        :return: a roman number with the difference of the two numbers
        """
        other_number = self._try_to_get_the_other_number(other)
        return RomanNumber.to_roman(self.to_arab() - other_number)

    def __rsub__(self, other):
        """
        Subtract a roman number, from another  number (roman or not)
        :param other: an integer / roman number
        :return: a roman number with the difference of the two numbers
        """
        other_number = self._try_to_get_the_other_number(other)
        return RomanNumber.to_roman(other_number - self.to_arab())

    def __mul__(self, other):
        """
        Multiply a roman number, with another  number (roman or not)
        :param other: an integer / roman number
        :return: a roman number with the multiplication of the two numbers
        """
        other_number = self._try_to_get_the_other_number(other)
        return RomanNumber.to_roman(self.to_arab() * other_number)

    def __rmul__(self, other):
        """
        Multiply a number (roman or not), with a roman number
        :param other: an integer / roman number
        :return: a roman number with the multiplication of the two numbers
        """
        return self * other

    def __truediv__(self, other):
        """
        Divide a roman number, with a number (roman or not)
        :param other: an integer / roman number
        :return: a roman number with the division of the two numbers
        """
        other_number = self._try_to_get_the_other_number(other)
        return RomanNumber.to_roman(self.to_arab() / other_number)

    def __rtruediv__(self, other):
        """
        Divide a number (roman or not), with a roman number
        :param other: an integer / roman number
        :return: a roman number with the division of the two numbers
        """
        other_number = self._try_to_get_the_other_number(other)
        return RomanNumber.to_roman(other_number / self.to_arab())

    def __lt__(self, other):
        """
        Return if the left number is smaller than the right one
        :param other: an integer / roman number
        :return: Boolean
        """
        other_number = self._try_to_get_the_other_number(other)
        return self.to_arab() < other_number

    def __gt__(self, other):
        """
        Return if the left number is greater than the right one
        :param other: an integer / roman number
        :return: Boolean
        """
        other_number = self._try_to_get_the_other_number(other)
        return self.to_arab() > other_number

    def __le__(self, other):
        """
        Return if the left number is smaller than the right one or equal to it
        :param other: an integer / roman number
        :return: Boolean
        """
        other_number = self._try_to_get_the_other_number(other)
        return self.to_arab() <= other_number

    def __ge__(self, other):
        """
        Return if the left number is greater than the right one or equal to it
        :param other: an integer / roman number
        :return: Boolean
        """
        other_number = self._try_to_get_the_other_number(other)
        return self.to_arab() >= other_number

    def __ne__(self, other):
        """
        Return if the left number is not equal to the right one
        :param other: an integer / roman number
        :return: Boolean
        """
        other_number = self._try_to_get_the_other_number(other)
        return self.to_arab() != other_number

    def __eq__(self, other):
        """
        Return if the left number is  equal to the right one
        :param other: an integer / roman number
        :return: Boolean
        """
        other_number = self._try_to_get_the_other_number(other)
        return self.to_arab() == other_number

    def __str__(self):
        """
        String representation of a roman number
        :return: a string
        """
        return self._roman

    def __repr__(self):
        """
        String representation of a roman number
        :return:  a string
        """
        return f"<RomanNumber (roman:{self._roman}, arab:{self._arab})>"

    def get_roman(self):
        return self._roman

    def _try_to_get_the_other_number(self, other):
        """Given the other number, checks its type and returns the arab value."""
        if isinstance(other, str) and not RomanNumber.is_valid(other):
            raise ValueError("The roman number is not valid.")
        elif not isinstance(other, int) and not isinstance(other, RomanNumber) and not isinstance(other, str):
            raise TypeError("The type of the roman number is invalid. It should be the number in arab or roman.")

        if isinstance(other, RomanNumber):
            return other.to_arab()
        elif isinstance(other, str):
            return RomanNumber(other).to_arab()
        else:
            return other

    def to_arab(self):
        """
        Turn a roman number to an arab number
        :return: an integer
        """
        arab = 0
        i = 0

        while i < len(self._roman):
            # Getting value of symbol [i]
            symbol = ROMAN_NUMBERS_DICT.get(self._roman[i])

            if (i + 1) < len(self._roman):
                # Getting value of next symbol
                next_symbol = ROMAN_NUMBERS_DICT.get(self._roman[i + 1])

                # Comparing both values:
                # They are in descending order
                # If the current symbol is gte than the next => The entire symbol is a vlalue by itself
                # Else, I take the next symbol and subtract the current symbol to it (e.g IX -> X - I -> 10 - 1)
                if symbol >= next_symbol:
                    arab += symbol
                    i += 1
                else:
                    arab += next_symbol - symbol
                    i += 2
            else:
                arab += symbol
                i += 1

        return arab

    @staticmethod
    def is_valid(string):
        """
        Check if a string is a valid roman number
        :param string: a string to validate
        :return: Boolean
        """
        roman_match = re.match("^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", string, flags=re.IGNORECASE)
        return string and isinstance(string, str) and roman_match is not None

    @staticmethod
    def to_roman(number):
        """
        Turn an integer to a roman number (string)
        :param number: an integer
        :return:
        """
        roman = ''
        while number > 0:
            for r, i in ROMAN_NUMBERS_TABLE:
                while number >= i:
                    roman = roman + r
                    number -= i
        return RomanNumber(roman)
