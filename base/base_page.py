import time

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config.links import Links


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=0.5)
        self.url = None

    def action_chains(self):
        return ActionChains(self.driver)

    def open_home_page(self):
        return self.driver.get(Links.HOME_PAGE_URL)

    def find_page_element(self, args):
        self.wait.until(
            EC.visibility_of_element_located(args)
        )
        return self.driver.find_element(*args)

    def find_element_without_wait(self, args):
        return self.driver.find_element(*args)

    def find_page_elements(self, args):
        self.wait.until(
            EC.visibility_of_element_located(args)
        )
        return self.driver.find_elements(*args)

    def click_to_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def type_text(self, text, locator):
        element = self.wait.until(EC.visibility_of_element_located(*locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(*locator))
        return element.text

    def elements_is_present(self, elements):
        return self.wait.until(EC.presence_of_all_elements_located(elements))

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(*locator))
            return True
        except TimeoutException:
            return False

    def scroll_page_to_the_end(self):
        self.action_chains().send_keys(Keys.END).perform()

    def scroll_page_down(self):
        self.action_chains().send_keys(Keys.PAGE_DOWN).perform()

    def scroll_page_up(self):
        self.action_chains().send_keys(Keys.PAGE_UP).perform()

    # # не  скролит почему-то
    # def scroll_page_to_the_element(self, locator):
    #     element = self.find_page_element(locator)
    #     self.action_chains().scroll_to_element(element)

    def scroll_page_to_the_element_by_js(self, locator):
        element = self.find_page_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # to be sure that element is present
        self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def get_url(self):
        return self.driver.current_url()

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()
