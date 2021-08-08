class LimitedList:
    """List that can hold a maximum number of elements. It is passed when the LimitedList is initialized."""

    def __init__(self, max_num_of_elements):
        self._max_num_of_elements = max_num_of_elements
        self._elements = []

    def __getitem__(self, index):
        """Given the index, it tries to return the element in that index."""
        return self._elements[index]

    def __setitem__(self, index, value):
        """Given the index and a new value, it tries to update the element entering by index."""
        self._elements[index] = value

    def __str__(self):
        """String representation of the LimitedList"""
        return str(self._elements)

    def __eq__(self, other_list):
        """Equal comparison between the list of elements and another list."""
        return isinstance(other_list, list) and self._elements == other_list

    def append(self, element):
        """
        Appends the new element to the list of elements. If the object reaches its limit, the 1st member is erased.
        """
        self._elements.append(element)
        if len(self._elements) > self._max_num_of_elements:
            self._elements = self._elements[1:]


def test_append_method():
    """Some tests for the initialization and the append method."""
    my_list = LimitedList(3)
    assert my_list == []
    [my_list.append(elem) for elem in [5, 2, 10]]
    assert my_list == [5, 2, 10]
    my_list.append("hello")
    assert my_list == [2, 10, "hello"]
    print("All append tests passed!")


def test_accessing_by_index():
    """Some tests checking the __getitem and __setitem__ implementations."""
    my_list = LimitedList(3)
    my_list.append(4)
    my_list.append(6)
    assert my_list == [4, 6]
    my_list[1] = "changed"
    assert my_list == [4, "changed"]
    assert my_list[0] == 4
    print("All accessing by index tests passed!")


def main():
    """Main function that runs some tests."""
    test_append_method()
    test_accessing_by_index()


if __name__ == "__main__":
    main()
