"""
Try to spot the bugs!

Author: Omer Rosenbaum
"""


def calculate_bmi(weight, height):
    """calculates a person's BMI given the persons weight and height"""
    return weight / (height ** 2)


if __name__ == '__main__':
    patients = [(75, 1.81), (82, 1.76), (95, 1.72)]

    for weight, height in patients:
        # ERROR: weight, height = patients[0]
        # The line above, was taking the same weight and height in every iteration.
        bmi = calculate_bmi(weight, height)
        # bmi = calculate_bmi(height, weight) this was wrong because it didn't respect the order of the parameters
        print("Patient's BMI is: %f" % bmi)
