from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
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
    @allure.step("page title locator generator")
    def choose_page_title_locator(title):
        locator = f"//span[@class='base' and @data-ui-id='page-title-wrapper' and text()='{title}']"
        title_locator = (By.XPATH, locator)
        return title_locator

    @allure.step("get women store catalog button element")
    def get_women_store_page_element(self):
        return self.find_page_element(self.WOMEN_PAGE)

    @allure.step("get women tops store catalog button element")
    def get_women_store_tops_page_element(self):
        return self.find_page_element(self.WOMEN_TOPS_PAGE)

    @allure.step("get women tops jacket store catalog button element")
    def get_women_tops_jacket_page_element(self):
        return self.find_page_element(self.WOMEN_TOPS_JACKETS_PAGE)

    @allure.step("get women store tops hoodies catalog button element")
    def get_women_tops_hoodies_page_element(self):
        return self.find_page_element(self.WOMEN_TOPS_HOODIES_PAGE)

    @allure.step("get women store tops tees catalog button element")
    def get_women_tops_tees_page_element(self):
        return self.find_page_element(self.WOMEN_TOPS_TEES_PAGE)

    @allure.step("get women store tops bras catalog button element")
    def get_women_tops_bras_page_element(self):
        return self.find_page_element(self.WOMEN_TOPS_BRA_PAGE)

    @allure.step("get women store bottoms catalog button element")
    def get_women_store_bottoms_page_element(self):
        return self.find_page_element(self.WOMEN_BOTTOM_PAGE)

    @allure.step("get women store bottoms pants catalog button element")
    def get_women_bottoms_pants_page_element(self):
        return self.find_page_element(self.WOMEN_BOTTOM_PANTS_PAGE)

    @allure.step("get women store bottoms shorts catalog button element")
    def get_women_store_bottoms_shorts_page_element(self):
        return self.find_page_element(self.WOMEN_BOTTOM_SHORTS_PAGE)

    @allure.step("open women store catalog page")
    def open_women_store_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).click().perform()

    @allure.step("open women store tops catalog page")
    def open_women_tops_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_tops_page_element()).click().perform()

    @allure.step("open women store tops jacket catalog page")
    def open_women_tops_jacket_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_tops_jacket_page_element()).click().perform()

    @allure.step("open women store tops hoodies catalog page")
    def open_women_tops_hoodies_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_tops_hoodies_page_element()).click().perform()

    @allure.step("open women store tops tees catalog page")
    def open_women_tops_tees_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_tops_tees_page_element()).click().perform()

    @allure.step("open women store catalog page")
    def open_women_tops_bras_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_tops_bras_page_element()).click().perform()

    @allure.step("open women store bottoms catalog page")
    def open_women_bottoms_page(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_bottoms_page_element()).perform()

    @allure.step("open women store bottoms pants catalog page")
    def open_women_bottoms_pants(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_bottoms_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_bottoms_pants_page_element()).click().perform()

    @allure.step("open women store bottoms shorts catalog page")
    def open_women_bottoms_shorts(self):
        self.action_chains().move_to_element(self.get_women_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_bottoms_page_element()).perform()
        self.action_chains().move_to_element(self.get_women_store_bottoms_shorts_page_element()).click().perform()

    @allure.step("check that product cards are present on the catalog page")
    def product_cards_are_present(self):
        return len(self.find_page_elements(self.PRODUCT_CARDS_LIST))

    @allure.step("check that product cards are present in the hot sellers list")
    def product_cards_are_present_in_hot_sellers_list(self):
        self.scroll_page_to_the_element_by_js(self.HOT_SELLERS_CARDS_LIST)
        return len(self.find_page_elements(self.HOT_SELLERS_CARDS_LIST))

    @allure.step("this method taking page title locator, it is flexiable method can get any page title")
    def get_page_title(self, title):
        element = self.choose_page_title_locator(title)
        element = self.find_page_element(element)
        return element
