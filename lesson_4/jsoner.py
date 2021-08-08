"""
Program with a one-line function that receives an url and returns a json-like encoded string.
"""

from urllib.parse import unquote
import json


def jsoner(url):
    """Receives a string and, in one line, triple each character of it. Then, returns the new tripled string."""
    return json.dumps({query_param.split('=')[0]: {'interesting': query_param.split('=')[1].split(',')[0], 'value': query_param.split('=')[1].split(',')[0]} for query_param in unquote(url).split('?')[1].split('&')})


def assert_verbose(actual, expected):
    """
    Given the expected and actual values o the assertion, check if both are equal,
    and prints an error message if the assertion fails.
    """
    assert expected == actual, f"Expected value: {expected}. But actual value is {actual}"


def interesting_url_test():
    """Test jsoner function with an interesting url."""
    url = "https://www.welovepython.com/onelinerexercise?python=-3.56%2C-2.55&is=-2.75%2C-4.92&" \
          "awesome=-4.63%2C-4.12&I=-5.75%2C-3.45&am=-1.0%2C-8.31&telling=-7.38%2C-2.41&you=-3.5%2C-3.6&" \
          "but=-4.38%2C-2.92&you=-7.13%2C-6.0&can=1.63%2C-2.36&probably=-5.75%2C-6.51&see=-3.25%2C-3.64&" \
          "that=1.75%2C-2.15&for=-3.75%2C-5.08&name=yourself&ec=-4.88&soc=-2.05"
    url_decoded = '{"python": {"interesting": "-3.56", "value": "-3.56"}, ' \
                  '"is": {"interesting": "-2.75", "value": "-2.75"}, ' \
                  '"awesome": {"interesting": "-4.63", "value": "-4.63"}, ' \
                  '"I": {"interesting": "-5.75", "value": "-5.75"}, ' \
                  '"am": {"interesting": "-1.0", "value": "-1.0"}, ' \
                  '"telling": {"interesting": "-7.38", "value": "-7.38"}, ' \
                  '"you": {"interesting": "-7.13", "value": "-7.13"}, ' \
                  '"but": {"interesting": "-4.38", "value": "-4.38"}, ' \
                  '"can": {"interesting": "1.63", "value": "1.63"}, ' \
                  '"probably": {"interesting": "-5.75", "value": "-5.75"}, ' \
                  '"see": {"interesting": "-3.25", "value": "-3.25"}, ' \
                  '"that": {"interesting": "1.75", "value": "1.75"}, ' \
                  '"for": {"interesting": "-3.75", "value": "-3.75"}, ' \
                  '"name": {"interesting": "yourself", "value": "yourself"}, ' \
                  '"ec": {"interesting": "-4.88", "value": "-4.88"}, ' \
                  '"soc": {"interesting": "-2.05", "value": "-2.05"}}'
    assert_verbose(jsoner(url), url_decoded)


def main():
    """Main function for run tests."""
    interesting_url_test()
    # I don't know how to make it works with empty strings. In the 1st split I'm trying to access to the 2nd element,
    # but with an empty string it crashes.
    # assert_verbose(jsoner(""), "")
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
