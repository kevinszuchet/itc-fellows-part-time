import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    # beforeEach
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_title(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()

    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    # afterEach
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
