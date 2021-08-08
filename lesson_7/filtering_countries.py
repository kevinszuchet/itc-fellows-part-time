"""
The annoying users from World Map keep sending us these ridiculous countries. Apparently, they also forgot that only
countries whose name either begin with 'i' or 'f', or end with 'd' or 'm'.
We need to have a function called filtered_world_map that returns a corrected list – where every country's name
begins with an uppercase letter, and the remaining letters are lowercase, and filters irrelevant countries.
"""

BEGINNINGS = ['i', 'f']
ENDINGS = ['d', 'm']


# Filters 'irrelevant' countries
def filtered_world_map(countries): return list(map(lambda country: country.capitalize(), (filter(lambda country: country[0].lower() in BEGINNINGS or country[-1].lower() in ENDINGS, countries))))


def main():
    """Main function that runs a test."""
    assert filtered_world_map(['ISRAEL', 'france', 'engLand', 'Brazil']) == ['Israel', 'France', 'England']
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
