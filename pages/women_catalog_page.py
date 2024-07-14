from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
import pytest


class WomenCatalogPage(BasePage):
    # elements of subpages in woman catalog
    WOMEN_PAGE = (By.ID, "ui-id-4")
    WOMEN_TOPS_PAGE = (By.ID, "ui-id-9")
    WOMEN_TOPS_JACKETS_PAGE = (By.ID, "ui-id-11")
    WOMEN_TOPS_HOODIES_PAGE = (By.ID, "ui-id-12")
    WOMEN_TOPS_TEES_PAGE = (By.ID, "ui-id-13")
    WOMEN_TOPS_BRA_PAGE = (By.ID, "ui-id-14")
    WOMEN_BOTTOM_PAGE = (By.ID, "ui-id-10")
    WOMEN_BOTTOM_PANTS_PAGE = (By.ID, "ui-id-15")
    WOMEN_BOTTOM_SHORTS_PAGE = (By.ID, "ui-id-16")
    PRODUCT_CARDS_LIST = (By.XPATH, "//ol[@class='products list items product-items']/li")

    # elements of woman catalog page
    HOT_SELLERS = (By.XPATH, "//ol[@class='product-items widget-product-grid']")
    HOT_SELLERS_CARDS_LIST = (By.XPATH, "//ol[@class='product-items widget-product-grid']/li")

    @staticmethod
    def choose_page_title_locator(title):
        locator = f"//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='{title}']"
        title_locator = (By.XPATH, locator)
        return title_locator

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_women_store_page_element(self):
        return self.find_page_element(self.WOMEN_PAGE)

    def get_women_store_tops_page_element(self):
        return self.find_page_element(self.WOMEN_TOPS_PAGE)

    def get_women_tops_jacket_page_element(self):
        return self.find_page_element(self.WOMEN_TOPS_JACKETS_PAGE)

    def get_women_tops_hoodies_page_element(self):
        return self.find_page_element(self.WOMEN_TOPS_HOODIES_PAGE)

    def get_women_tops_tees_page_element(self):
        return self.find_page_element(self.WOMEN_TOPS_TEES_PAGE)

    def get_women_tops_bras_page_element(self):
        return self.find_page_element(self.WOMEN_TOPS_BRA_PAGE)

    def get_women_store_bottoms_page_element(self):
        return self.find_page_element(self.WOMEN_BOTTOM_PAGE)

    def get_women_bottoms_pants_page_element(self):
        return self.find_page_element(self.WOMEN_BOTTOM_PANTS_PAGE)

    def get_women_store_bottoms_shorts_page_element(self):
        return self.find_page_element(self.WOMEN_BOTTOM_SHORTS_PAGE)

    def open_women_store_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).click().perform()

    def open_women_tops_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_tops_page_element()).click().perform()

    def open_women_tops_jacket_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_tops_jacket_page_element()).click().perform()

    def open_women_tops_hoodies_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_tops_hoodies_page_element()).click().perform()

    def open_women_tops_tees_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_tops_tees_page_element()).click().perform()

    def open_women_tops_bras_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_tops_bras_page_element()).click().perform()

    def open_women_bottoms_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_bottoms_page_element()).perform()

    def open_women_bottoms_pants(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_bottoms_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_bottoms_pants_page_element()).click().perform()

    def open_women_bottoms_shorts(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_bottoms_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_bottoms_shorts_page_element()).click().perform()

    def product_cards_are_present(self):
        return len(self.find_page_elements(self.PRODUCT_CARDS_LIST))

    def product_cards_are_present_in_hot_sellers_list(self):
        self.scroll_page_to_the_element_by_js(self.HOT_SELLERS_CARDS_LIST)
        return len(self.find_page_elements(self.HOT_SELLERS_CARDS_LIST))

    def get_page_title(self, title):
        element = self.choose_page_title_locator(title)
        element = self.find_page_element(element)
        return element
