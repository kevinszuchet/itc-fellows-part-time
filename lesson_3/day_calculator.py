"""Program that given a number of days, returns the ISO date of that number of days from now."""

from datetime import datetime, timedelta


def day_calculator(number_of_days):
    """Takes a number of days, prints a new date with some number of days from now in ISO format, and returns it."""
    new_date = (datetime.now() + timedelta(days=number_of_days)).isoformat()
    print(new_date)
    return new_date


def main():
    """"Main function that prints some cases."""
    day_calculator(5)
    day_calculator(30)
    day_calculator(365)
    day_calculator(31)


if __name__ == "__main__":
    main()
