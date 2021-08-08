"""Run tests for the roman number class implementation."""
import sys

from roman_number import RomanNumber


def arithmetic_tests():
    """Tests arithmetic operations."""
    xii = RomanNumber("XII")
    xl = 40
    vi = 6

    assert xii + xl == 52 == xl + xii
    assert xl - xii == 28
    assert xii - vi == 6
    assert xii / vi == 2


def comparison_tests():
    """Tests about comparison operators."""
    xii = RomanNumber("XII")
    vi = 6

    assert RomanNumber.to_roman(4) == "IV"
    assert RomanNumber.to_roman(4) == RomanNumber("IV")

    assert xii > vi
    assert xii != vi
    assert xii >= RomanNumber("XII")
    assert xii == 12
    assert str(xii) == "XII"


def validation_tests():
    """Validation methods tests."""
    xii = RomanNumber("XII")
    # It won't be created because I put the validation in the constructor to avoid having an invalid roman numbers.
    # invalid_roman_number = RomanNumber("MXIIXII")
    assert RomanNumber.is_valid(xii.get_roman())
    assert not RomanNumber.is_valid("MXIIXII")


def representation_tests():
    """__str__ and __repr__ tests."""
    xii = RomanNumber("XII")
    assert str(xii) == "XII"
    assert repr(xii) == "<RomanNumber (roman:XII, arab:12)>"


def main():
    """Main function to run tests."""
    arithmetic_tests()
    comparison_tests()
    validation_tests()
    representation_tests()
    print("All tests passed!")


if __name__ == '__main__':
    main()
