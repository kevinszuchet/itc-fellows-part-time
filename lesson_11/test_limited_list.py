import pytest as pytest

from limited_list import LimitedList


# Setup
def limited_list_with_2_elements():
    ll = LimitedList(2)
    ll.append("Kevin")
    ll.append("Szuchet")
    return ll


def test_limited_list_initialized_successfully_with_correct_limit():
    ll = LimitedList(1)
    assert ll._limit == 1

    ll = LimitedList(2)
    assert ll._limit == 2


def test_limited_list_raise_value_error_because_of_the_limit_type():
    with pytest.raises(ValueError, match=r"limit received is not an integer"):
        ll = LimitedList("Hello Moto!")


def test_limited_list_raise_value_error_because_the_limit_is_less_than_1():
    with pytest.raises(ValueError, match=r"Minimum limit allowed"):
        LimitedList(0)

    with pytest.raises(ValueError, match=r"Minimum limit allowed"):
        LimitedList(-1)


def test_regular_append():
    ll = limited_list_with_2_elements()
    assert ll._list == ["Kevin", "Szuchet"]


def test_limited_append():
    ll = limited_list_with_2_elements()
    ll.append("Hello")
    ll.append("World!")
    assert ll._list == ["Hello", "World!"]


def test_access_list_with_invalid_type_index_raises_value_error():
    ll = limited_list_with_2_elements()

    with pytest.raises(ValueError, match="index received is not an integer"):
        ll["Kevin"]


def test_access_list_with_negative_index_raises_value_error():
    ll = limited_list_with_2_elements()

    with pytest.raises(ValueError, match="Negative index"):
        ll[-1]


def test_access_list_with_index_grater_than_the_size_raises_value_error():
    ll = limited_list_with_2_elements()

    with pytest.raises(ValueError, match=r"Invalid index given: \d+, max allowed"):
        ll[2]


def test_access_list_and_set_value_with_invalid_type_index_raises_value_error():
    ll = limited_list_with_2_elements()

    with pytest.raises(ValueError, match="index received is not an integer"):
        ll["Kevin"] = "Modified Kevin"


def test_access_list_and_set_value_with_negative_index_raises_value_error():
    ll = limited_list_with_2_elements()

    with pytest.raises(ValueError, match="Negative index"):
        ll[-1] = "Lastname"


def test_access_list_and_set_value_with_index_grater_than_the_size_raises_value_error():
    ll = limited_list_with_2_elements()

    with pytest.raises(ValueError, match=r"Invalid index given: \d+, max allowed"):
        ll[10] = "Hello World!"
