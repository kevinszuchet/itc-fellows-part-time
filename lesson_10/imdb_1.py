"""
Program that takes the top 250 movies from IMDB and shows some details of each one in different outputs.
"""

import requests
import time
import conf as CFG
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class IMDbScrapper:
    def __init__(self):
        self.base_url = CFG.IMDB_URL

    def _full_path(self, endpoint):
        """Given an endpoint, returns the full path of the IMDB url"""
        return urljoin(self.base_url, endpoint)

    def _get(self, endpoint):
        """Given the endpoint, makes the request to the IMDB site."""
        full_path = self._full_path(endpoint)
        return requests.get(full_path)

    def _get_top_250(self):
        """Returns the response of the get to the tp 250 chart page."""
        return self._get(CFG.IMDB_CHART_ENDPOINT)

    def _get_movie_details(self, endpoint):
        """Given the movie endpoint, returns the response of the GET to the detail page."""
        return self._get(endpoint)

    def _get_titles(self):
        """Gets the column with the title and link to detail page of each movie. Returns the complete list."""
        top_250_page = self._get_top_250()
        if top_250_page:
            top_250_soup = BeautifulSoup(top_250_page.content, 'html.parser')
            return top_250_soup.find_all("td", class_="titleColumn")

    def _get_directors(self, title_column):
        """Given the title column element, gets the movie details and returns the name of the director."""
        movie_details = self._get_movie_details(title_column.a.attrs['href'])
        if movie_details:
            movie_details_soup = BeautifulSoup(movie_details.content, 'html.parser')
            credit_summary = movie_details_soup.find("div", class_="credit_summary_item")
            return credit_summary.a.text

    def show_titles_and_directors(self):
        """Get the chart page of IMDB, iterates over the top 250 titles,
        and show each one with its correspondent director."""
        for i, title_column in enumerate(self._get_titles()):
            directors = self._get_directors(title_column)
            if directors:
                print(f"{i + 1} - {title_column.a.text} - {directors}")


def main():
    """Main function. Shows the titles with directors, and calculates (and shows) how long the program takes."""
    before = time.time()
    IMDbScrapper().show_titles_with_directors()
    after = time.time()
    print("Time taken: {:.1f} ms".format((after - before) * 1000))


if __name__ == '__main__':
    """Executes main function"""
    main()
