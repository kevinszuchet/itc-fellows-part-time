"""
This is a program that takes the sentence "We were more than just a slice" and print out different sliced strings.
"""

SENTENCE_TO_SLICE = "We were more than just a slice"


def first_slice():
    return SENTENCE_TO_SLICE[0:6]


def second_slice():
    return SENTENCE_TO_SLICE[4:-2]


def third_slice():
    return SENTENCE_TO_SLICE[0::2]


def fourth_slice():
    return SENTENCE_TO_SLICE[3:-1:2]


def fifth_slice():
    return SENTENCE_TO_SLICE[::-1]


SLICE_FUNCTIONS = [first_slice, second_slice, third_slice, fourth_slice, fifth_slice]


def print_slices():
    """Print out some string slices"""

    for i, fn in enumerate(SLICE_FUNCTIONS):
        print(f"{i + 1}) {fn()}")


if __name__ == '__main__':
    assert first_slice() == 'We wer'
    assert second_slice() == 'ere more than just a sli'
    assert third_slice() == 'W eemr hnjs  lc'
    assert fourth_slice() == 'wr oeta utasi'
    assert fifth_slice() == 'ecils a tsuj naht erom erew eW'

    print('--- All tests passed ---')
    print_slices()
