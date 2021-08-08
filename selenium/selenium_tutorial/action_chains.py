# Python Selenium Tutorial - Tech Withh Tim
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


def main():
    driver = webdriver.Chrome()

    driver.get("https://orteil.dashnet.org/cookieclicker/")

    driver.implicitly_wait(5)

    cookie = driver.find_element_by_id("bigCookie")
    cookie_count = driver.find_element_by_id("cookies")
    items = [driver.find_element_by_id(f"productPrice{i}") for i in range(1, -1, -1)]

    actions = ActionChains(driver)
    actions.click(cookie)

    for i in range(5000):
        # Necessary to perform the actions
        actions.perform()
        count = int(cookie_count.text.split()[0])
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
