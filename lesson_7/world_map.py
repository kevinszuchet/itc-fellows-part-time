"""
Returns a corrected list – where every country’s name begins with an uppercase letter,
and the remaining letters are lowercase,
"""
def world_map(countries): return list(map(lambda country: country.capitalize(), countries))


def main():
    """Main function that runs a test."""
    assert world_map(['ISRAEL', 'france', 'engLand']) == ['Israel', 'France', 'England']
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
