from selenium.common.exceptions import NoSuchElementException


def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False

