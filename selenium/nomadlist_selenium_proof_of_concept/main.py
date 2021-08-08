import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

NOMAD_LIST_URL = "https://nomadlist.com/"
SCROLL_PAUSE_TIME = 5


def get_scroll_height(driver):
    return driver.execute_script("return document.body.scrollHeight")


def main():
    # driver = webdriver.Chrome()
    # driver.get(NOMAD_LIST_URL)

    # Get scroll height
    # scroll_height = get_scroll_height(driver)

    li_cities = []

    time.sleep(2)

    page_source = requests.get(NOMAD_LIST_URL).content
    soup = BeautifulSoup(page_source, "html.parser")
    action_regex = re.compile(r'(label|rating)-(\w+)-score')
    cities = []
    for li in soup.find_all(attrs={'data-type': 'city'})[:1]:
        text = li.find(class_="text")
        city = text.h2.text if text.h2 else "-"
        country = text.h3.text if text.h3 else "-"
        action_span_container = li.find(class_="action")
        description = action_span_container.p.text
        actions = {}
        for action_span in action_span_container.find_all("span"):
            score_class_name = action_span['class'][0]
            match = action_regex.match(score_class_name)
            if match:
                span_type = match.group(1)
                action_name = match.group(2)
                action = actions.get(action_name, {})
                # TODO review where the 'All' (next to Overall) come from and replace it by nothing!
                action.update({span_type: action_span.text or '-'})
                if span_type == "rating":
                    rating_percent = action_span.span.attrs["style"].replace("width:", "").replace("%", "")
                    rating_percent = float(rating_percent)
                    action.update({'rating_percent': rating_percent})
                actions.update({action_name: action})

        attributes_span = li.find(class_="attributes")
        attributes = []
        for attribute_element_span in attributes_span.find_all("span", class_="element"):
            attribute = {}
            position = attribute_element_span['class'][1]
            if position == "bottom-left":
                weather_emoji = attribute_element_span.find("span", class_="weather-emoji").text
                temperature = attribute_element_span.find("span", class_="temperature")
                attribute.update({'temperature': {}, 'heat_index': {}})
                for heat_index_span in temperature.find("span", class_="label-heat-index").find_all("span", class_="value"):
                    attribute['heat_index'].update({heat_index_span['class'][-1]: heat_index_span.text})
                for temperature_span in temperature.find_all("span", class_="value"):
                    # TODO review. It takes all the span.value (find siblings)
                    attribute['temperature'].update({temperature_span['class'][-1]: temperature_span.text})
                air_quality = attribute_element_span.find("span", class_="air_quality")
                attribute.update({air_quality.find("span", class_="above").text: air_quality.find("span", class_="value").text})
            elif position == "top-left":
                # TODO complete this
                pass
            elif position == "bottom-right":
                attribute.update({'price': attribute_element_span.span.text})
            elif position == "top-right":
                internet_span = attribute_element_span.find("span", class_="right")
                print("internet_span", internet_span)
                attribute.update({'internet': {'value': internet_span.find("span", class_="value").text, 'unit': internet_span.find("span", class_="mbps").text}})

            attributes.append(attribute)

        cities.append({'name': city, 'country': country, 'description': description, 'actions': actions, 'attributes': attributes})
        print(cities)

    return

    for i in range(5):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_scroll_height = get_scroll_height(driver)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        cities = soup.find_all(attrs={'data-type': 'city'})
        li_cities += cities

        if new_scroll_height == scroll_height:
            # If heights are the same it will exit the function
            break
        scroll_height = new_scroll_height

    print(len(li_cities))
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
