"""
Program that takes the top 250 movies from IMDB and shows some details of each one in different outputs.
"""

import grequests
import requests
import time
import conf as CFG
import logging
import re
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class Logger:
    def __init__(self):
        # Initiating the logger object
        self.logger = logging.getLogger(__name__)

        # Set the level of the logger.
        self.logger.setLevel(logging.DEBUG)

        # Format the logs structure so that every line would include the time, name, level name and log message
        formatter = logging.Formatter(CFG.LOG_FORMAT)

        # Create a file handler and add it to logger
        file_handler = logging.FileHandler(CFG.LOG_FILE)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Create a stream handler and add it to logger
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)


class IMDbScrapper:
    def __init__(self):
        self.base_url = CFG.IMDB_URL
        self.logger = Logger().logger

    def _full_path(self, endpoint):
        """Given an endpoint, returns the full path of the IMDB url"""
        return urljoin(self.base_url, endpoint)

    def _exception_handler(self, r, exception):
        """Log the error message using the configured logger."""
        self.logger.error(f"Something went wrong doing the request: {exception}")

    def _check_response(self, response):
        """Check the status of the response and try to raise an error. If there is an exception, logs the message."""
        try:
            response.raise_for_status()
        except requests.RequestException as e:
            self._exception_handler(response, e)
            raise e

    def _get_top_250(self):
        """Returns the response of the get to the tp 250 chart page."""
        full_path = self._full_path(CFG.IMDB_CHART_ENDPOINT)
        response = requests.get(full_path)

        self._check_response(response)

        if response.status_code == requests.codes.ok:
            return response

    def _get_movies_details(self, titles_columns):
        """
        Given the movie rows, takes the url of each title.
        Then, returns the response of doing a GET to the detail page of each one.
        """
        reqs = (grequests.get(self._full_path(title_column.a.attrs['href'])) for title_column in titles_columns)
        responses = grequests.map(reqs, size=CFG.BATCH_SIZE, exception_handler=self._exception_handler)
        self.logger.info("Successfully map all the reqs with grequests.")
        return responses

    def _get_titles(self):
        """Gets the column with the title and link to detail page of each movie. Returns the complete list."""
        top_250_page = self._get_top_250()
        if top_250_page:
            self.logger.info("Successfully fetched the top 250 page.")
            return BeautifulSoup(top_250_page.content, 'html.parser').find_all("td", class_="titleColumn")
        else:
            self.logger.critical("The top 250 page is empty.")

    def _get_title_and_directors(self, movie_details):
        """Given the title column element, gets the movie details and returns the name of the director."""
        movie_details_soup = BeautifulSoup(movie_details.content, 'html.parser')
        title_wrapper = movie_details_soup.find("div", class_="title_wrapper")
        credit_summary = movie_details_soup.find("div", class_="credit_summary_item")

        if not title_wrapper:
            self.logger.error(f"Something went wrong finding the title ({title_wrapper}).")
            return

        if not credit_summary:
            self.logger.error(f"Something went wrong finding the directors names ({credit_summary}).")
            return

        title = re.sub(r"\(\d+\)", "", title_wrapper.h1.text).strip()
        directors = re.sub(r"\(\w+\)", "", credit_summary.a.text).strip()
        self.logger.debug(f"Got it! Title and directors: {title} - {directors}")
        return title, directors

    def show_titles_with_directors(self):
        """Get the chart page of IMDB, iterates over the top 250 titles,
        and show each one with its correspondent director."""
        titles = self._get_titles()
        self.logger.debug(f"Top 250 titles: {titles}")

        for i, response in enumerate(self._get_movies_details(titles)):
            try:
                self._check_response(response)
                self.logger.debug(f"Successfully fetched movie details: {response}.")
                title, directors = self._get_title_and_directors(response)
                if title and directors:
                    rank = i + 1
                    print(f"{rank} - {title} - {directors}")
                else:
                    self.logger.error(f"Missing the title or directors for the movie {i} in the ranking.")
            except requests.RequestException:
                continue

        self.logger.info("--- Done! ---")


def main():
    """Main function. Shows the titles with directors, and calculates (and shows) how long the program takes."""
    before = time.time()
    IMDbScrapper().show_titles_with_directors()
    after = time.time()
    print("Time taken: {:.1f} ms".format((after - before) * 1000))


if __name__ == '__main__':
    """Executes main function"""
    main()
