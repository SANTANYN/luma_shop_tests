from selenium.webdriver.common.by import By
import allure
from base.base_page import BasePage


class GearCatalogPage(BasePage):
    # Locators for the gear section
    GEAR_STORE_SECTION = (By.ID, "ui-id-6")
    GEAR_BAGS_SECTION = (By.ID, "ui-id-25")
    GEAR_FITNESS_SECTION = (By.ID, "ui-id-26")
    GEAR_WATCHES_SECTION = (By.ID, "ui-id-27")
    PRODUCT_PRICE = (By.XPATH, "//span[@class='price-wrapper ']/span[@class='price']")

    @allure.step("get gear store catalog button element")
    def get_gear_store_page_element(self):
        return self.find_page_element(self.GEAR_STORE_SECTION)

    @allure.step("get gear bags store catalog button element")
    def get_gear_store_bags_page_element(self):
        return self.find_page_element(self.GEAR_BAGS_SECTION)

    @allure.step("open gear store catalog page")
    def open_gear_store_page(self):
        self.action_chains().move_to_element(self.get_gear_store_page_element()).click().perform()

    @allure.step("open gear bags store  catalog page")
    def open_gear_bags_page(self):
        self.action_chains().move_to_element(self.get_gear_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_gear_store_bags_page_element()).click().perform()

    @allure.step("get product prices in gear bags store catalog page")
    def get_products_prices(self):
        list_of_prices = self.get_elements_text_by_list(self.PRODUCT_PRICE)
        return list_of_prices

