import pytest
from selenium import webdriver
import file
import present
from selenium.webdriver.common.by import By


@pytest.fixture
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.driver = chrome_driver
    return chrome_driver


def test_example(chrome_driver_init):
    chrome_driver_init.get("https://www.google.ru/")
    # file.find_element(chrome_driver_init, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    present.is_element_present(chrome_driver_init, By.XPATH, "//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[2]")
