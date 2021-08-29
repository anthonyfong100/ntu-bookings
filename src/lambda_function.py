import time

from selenium.webdriver.common.keys import Keys

from webdriver_wrapper import WebDriverWrapper


def lambda_handler(*args, **kwargs):
    driver = WebDriverWrapper()

    driver.get_url("http://example.com")
    example_text = driver.get_inner_html("(//div//h1)[1]")

    driver.close()

    return example_text
