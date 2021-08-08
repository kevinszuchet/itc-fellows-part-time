class LimitedList:
    def __init__(self, limit):
        """
        Create a Limited List with given limit
        :param limit: limit for number of integers in the list, integer expected with minimum limit of 1
        """
        if not isinstance(limit, int):
            raise ValueError(f'limit received is not an integer: {limit}')
        if limit < 1:
            raise ValueError(f'Minimum limit allowed: 1, given: {limit}')
        self._limit = limit
        self._list = []
        print("LimitedList created, limit:", limit)

    def append(self, value):
        """
        Append the given value to the end of the list.  If appending the value causes the
        size of LimitedList be larger than expected, the first element will be removed
        :param value: value to append
        """
        self._list.append(value)
        if len(self._list) > self._limit:
            self._list.pop(0)

    def _check_index(self, index):
        if not isinstance(index, int):
            raise ValueError(f'index received is not an integer: {index}')
        if index < 0:
            raise ValueError(f'Negative index index given: {index}')
        if index >= len(self._list):
            raise ValueError(f'Invalid index given: {index}, max allowed: {len(self._list)}')

    def __getitem__(self, index):
        """
        Get a value at the given index
        :param index: integer of valid index in the list
        :return: value at the given index
        """
        self._check_index(index)
        return self._list[index]

    def __setitem__(self, index, value):
        """
        Set the given value at the given index
        :param index: integer of valid index in the list
        :param value: value to set
        """
        self._check_index(index)
        self._list[index] = value
