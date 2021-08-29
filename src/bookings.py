import os
import time
from typing import Optional

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import constants as constants
from utils import is_valid_court_num, is_valid_time
from webdriver_wrapper import WebDriverWrapper


def login(driver: webdriver) -> None:
    driver.get(constants.LOGIN_URL.format(os.getenv("MATRIC_NUMBER")))

    # input username
    driver.find_element_by_xpath(constants.USERNAME_XPATH).send_keys(
        os.getenv("USERNAME")
    )

    # select student
    driver.find_element_by_xpath(constants.SELECT_STUDENT_XPATH).click()

    # click login button
    driver.find_element_by_xpath(constants.LOGIN_XPATH).click()

    time.sleep(1)

    # input password
    driver.find_element_by_xpath(constants.PASSWORD_XPATH).send_keys(
        os.getenv("PASSWORD")
    )

    # submit
    driver.find_element_by_xpath(constants.SUBMIT_XPATH).click()


def go_to_booking_page(driver: webdriver) -> None:
    BOOKING_URL_ROOT_PATH = constants.BOOKING_URL.format(
        os.getenv("MATRIC_NUMBER")
    )
    driver.get(BOOKING_URL_ROOT_PATH)
    driver.find_element_by_xpath(constants.BADMINTON_NORTH_HILL).click()


def gen_xpath_radio(start_time: int, court_number: int) -> str:
    if not is_valid_court_num(court_number) or not is_valid_time(start_time):
        raise ValueError(
            f"Court number should be an integer between 1 to 6, received:{court_number}"
        )
    time_offset = start_time - 8
    row_num = time_offset * 6 + court_number + 1
    data_num = 10 if court_number == 1 else 9
    return constants.BADMINTON_NEXT_WEEK.format(row_num, data_num)


def book(
    driver: webdriver, start_time: int, court_number: Optional[int]
) -> None:
    if court_number is None:
        court_numbers = [ix for ix in range(1, 7)]
    else:
        court_numbers = [court_number]

    for court_number in court_numbers:
        x_path = gen_xpath_radio(start_time, court_number)
        try:
            driver.find_element_by_xpath(x_path).click()
        except NoSuchElementException:
            print(
                f"xpath:{x_path} not exists, start_time:{start_time} court_number:{court_number}"
            )


def run():
    load_dotenv()
    START_TIME = 14
    COURT_NUMBER = 6
    # driver = WebDriverWrapper(
    #     chrome_browser_location="./bin/macOS/chromedriver"
    # )
    driver = webdriver.Chrome("./bin/macOS/chromedriver")
    login(driver)
    time.sleep(1)
    go_to_booking_page(driver)
    book(driver, START_TIME, COURT_NUMBER)


if __name__ == "__main__":
    run()
