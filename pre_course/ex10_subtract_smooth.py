import numpy as np


def subtract_smooth(x, y):
    resized_y = y.copy()
    resized_y.resize(x.shape)
    y_new = resized_y - median_filter(x, resized_y, 1.)
    return y_new


def median_filter(x, y, width):
    # Error: IndexError: boolean index did not match indexed array along dimension 0; dimension is 4 but
    # corresponding boolean dimension is 5
    # I searched in google about 'boolean index did not match indexed array along dimension'
    # I noticed that y_new has the same shape as y, but in this case x has another shape
    # The calculation inside the y brackets returns an array of booleans that has a different shape than y
    # Maybe we can fill with zeros the smallest array in order to keep all the data points but I'm not sure
    y_new = np.zeros(y.shape)
    for i in range(len(x)):
        y_new[i] = np.median(y[np.abs(x - x[i]) < width * 0.5])
    return y_new


print(subtract_smooth(np.array([1, 2, 3, 4, 5]), np.array([4, 5, 6, 8])))
