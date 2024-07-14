from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config.links import Links


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
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

    def find_page_elements(self, args):
        self.wait.until(
            EC.presence_of_all_elements_located(args)
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

    def get_url(self):
        return self.driver.current_url()

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()
