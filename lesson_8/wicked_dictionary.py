class WickedDictionary:
    """Acts like a normal dictionary, but whenever someone creates a new key, that key will be doubled."""

    def __init__(self):
        self._dict = {}

    def __getitem__(self, key):
        """Returns the value of the dict entering by the key."""
        return self._dict[key]

    def __setitem__(self, key, value):
        """Given a key and a value, creates a new entrance to the dictionary with a doubled key and the value."""
        self._dict.update({key * 2: value})

    def __str__(self):
        """String representation of the WickedDictionary"""
        return str(self._dict)

    def __eq__(self, another_dict):
        """Equal comparison between the wicked dict and another one."""
        return isinstance(another_dict, dict) and self._dict == another_dict


def main():
    """Main function that runs some tests."""
    my_dict = WickedDictionary()
    my_dict["hello"] = 12
    my_dict[2] = "test"
    assert my_dict == {'hellohello': 12, 4: 'test'}
    assert my_dict[4] == 'test'
    print("All tests passed!")


if __name__ == "__main__":
    main()
