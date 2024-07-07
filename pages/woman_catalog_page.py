from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators
from base.base_page import BasePage
import pytest


class WomanCatalogPage(BasePage):
    WOMAN_PAGE = (By.ID, "ui-id-4")
    WOMAN_TOPS_PAGE = (By.ID, "ui-id-9")
    WOMAN_TOPS_JACKETS_PAGE = (By.ID, "ui-id-11")
    WOMAN_TOPS_HOODIES_PAGE = (By.ID, "ui-id-12")
    WOMAN_TOPS_TEES_PAGE = (By.ID, "ui-id-13")
    WOMAN_TOPS_BRA_PAGE = (By.ID, "ui-id-14")
    WOMAN_BOTTOM_PAGE = (By.ID, "ui-id-10")
    WOMAN_BOTTOM_PANTS_PAGE = (By.ID, "ui-id-15")
    WOMAN_BOTTOM_SHORTS_PAGE = (By.ID, "ui-id-16")
    PRODUCT_CARDS_LIST = (By.XPATH, "//ol[@class='products list items product-items']/li")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_woman_store_page_element(self):
        return self.find_page_element(self.WOMAN_PAGE)

    def get_woman_store_tops_page_element(self):
        return self.find_page_element(self.WOMAN_TOPS_PAGE)

    def get_woman_tops_jacket_page_element(self):
        return self.find_page_element(self.WOMAN_TOPS_JACKETS_PAGE)

    def get_woman_tops_hoodies_page_element(self):
        return self.find_page_element(self.WOMAN_TOPS_HOODIES_PAGE)

    def get_woman_tops_tees_page_element(self):
        return self.find_page_element(self.WOMAN_TOPS_TEES_PAGE)

    def get_woman_tops_bras_page_element(self):
        return self.find_page_element(self.WOMAN_TOPS_BRA_PAGE)

    def get_woman_store_bottoms_page_element(self):
        return self.find_page_element(self.WOMAN_BOTTOM_PAGE)

    def get_woman_bottoms_pants_page_element(self):
        return self.find_page_element(self.WOMAN_BOTTOM_PANTS_PAGE)

    def get_woman_store_bottoms_shorts_page_element(self):
        return self.find_page_element(self.WOMAN_BOTTOM_SHORTS_PAGE)

    def open_woman_store_page(self):
        self.action_chains().move_to_element(self.get_woman_store_page_element()).click().perform()

    def open_woman_tops_page(self):
        self.action_chains().move_to_element(self.get_woman_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_store_tops_page_element()).click().perform()

    def open_woman_tops_jacket_page(self):
        self.action_chains().move_to_element(self.get_woman_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_tops_jacket_page_element()).click().perform()

    def open_woman_tops_hoodies_page(self):
        self.action_chains().move_to_element(self.get_woman_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_tops_hoodies_page_element()).click().perform()

    def open_woman_tops_tees_page(self):
        self.action_chains().move_to_element(self.get_woman_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_tops_tees_page_element()).click().perform()

    def open_woman_tops_bras_page(self):
        self.action_chains().move_to_element(self.get_woman_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_store_tops_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_tops_bras_page_element()).click().perform()

    def open_woman_bottoms_page(self):
        self.action_chains().move_to_element(self.get_woman_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_store_bottoms_page_element()).perform()

    def open_woman_bottoms_pants(self):
        self.action_chains().move_to_element(self.get_woman_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_store_bottoms_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_bottoms_pants_page_element()).click().perform()

    def open_woman_bottoms_shorts(self):
        self.action_chains().move_to_element(self.get_woman_store_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_store_bottoms_page_element()).perform()
        self.action_chains().move_to_element(self.get_woman_store_bottoms_shorts_page_element()).click().perform()

    def product_cards_are_present(self):
        return len(self.find_page_elements(self.PRODUCT_CARDS_LIST))

