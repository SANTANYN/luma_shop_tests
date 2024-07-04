from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class HomePage(BasePage):
    WOMEN_CLOTHES_PAGE = ("id", "ui-id-4")
    TOPS_MENU = (By.ID, "ui-id-9")
    JACKETS_MENU = (By.ID, "ui-id-12")

    def navigate_to_jackets(self):
        actions = ActionChains(self.driver)

        women_menu = self.driver.find_element(*self.WOMEN_CLOTHES_PAGE)
        tops_menu = self.driver.find_element(*self.TOPS_MENU)
        jackets_menu = self.driver.find_element(*self.JACKETS_MENU)

        actions.move_to_element(women_menu).perform()
        actions.move_to_element(tops_menu).perform()
        actions.move_to_element(jackets_menu).click().perform()