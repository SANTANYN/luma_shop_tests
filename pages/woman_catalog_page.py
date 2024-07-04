from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
        # self.woman_store_element = self.find_page_element(self.WOMAN_PAGE)
        # self.woman_tops_element = self.find_page_element(self.WOMAN_TOPS_PAGE)
        # self.woman_tops_jacket_element = self.find_page_element(self.WOMAN_TOPS_JACKETS_PAGE)
        # self.woman_tops_hoodies_element = self.find_page_element(self.WOMAN_TOPS_HOODIES_PAGE)
        # self.woman_tops_tees_element = self.find_page_element(self.WOMAN_TOPS_TEES_PAGE)
        # self.woman_tops_bras_element = self.find_page_element(self.WOMAN_TOPS_BRA_PAGE)
        # self.woman_bottoms_element = self.find_page_element(self.WOMAN_BOTTOM_PAGE)
        # self.woman_bottoms_pants_element = self.find_page_element(self.WOMAN_BOTTOM_PANTS_PAGE)
        # self.woman_bottoms_shorts_element = self.find_page_element(self.WOMAN_BOTTOM_SHORTS_PAGE)

    def open_woman_store_page(self):
        woman_store_element = self.driver.find_page_element(self.WOMAN_PAGE)
        self.action_chains().move_to_element(woman_store_element).click().perform()

    def open_woman_tops_page(self):
        woman_store_element = self.driver.find_page_element(self.WOMAN_PAGE)
        woman_tops_element = self.driver.find_page_element(self.WOMAN_TOPS_PAGE)

        self.action_chains().move_to_element(woman_store_element)
        self.action_chains().move_to_element(woman_tops_element).click().perform()

    def open_woman_tops_jacket_page(self):
        woman_store_element = self.find_page_element(self.WOMAN_PAGE)
        woman_tops_element = self.find_page_element(self.WOMAN_TOPS_PAGE)
        woman_tops_jacket_element = self.find_page_element(self.WOMAN_TOPS_JACKETS_PAGE)

        self.action_chains().move_to_element(woman_store_element).perform()
        self.action_chains().move_to_element(woman_tops_element).perform()
        self.action_chains().move_to_element(woman_tops_jacket_element).click().perform()

    def open_woman_tops_hoodies_page(self):
        woman_store_element = self.find_page_element(self.WOMAN_PAGE)
        woman_tops_element = self.find_page_element(self.WOMAN_TOPS_PAGE)
        woman_tops_hoodies_element = self.find_page_element(self.WOMAN_TOPS_HOODIES_PAGE)

        self.action_chains().move_to_element(woman_store_element).perform()
        self.action_chains().move_to_element(woman_tops_element).perform()
        self.action_chains().move_to_element(woman_tops_hoodies_element).click().perform()

    def open_woman_tops_tees_page(self):
        woman_store_element = self.find_page_element(self.WOMAN_PAGE)
        woman_tops_element = self.find_page_element(self.WOMAN_TOPS_PAGE)
        woman_tops_tees_element = self.find_page_element(self.WOMAN_TOPS_TEES_PAGE)

        self.action_chains().move_to_element(woman_store_element).perform()
        self.action_chains().move_to_element(woman_tops_element).perform()
        self.action_chains().move_to_element(woman_tops_tees_element).click().perform()

    def open_woman_tops_bras_page(self):
        woman_store_element = self.find_page_element(self.WOMAN_PAGE)
        woman_tops_element = self.find_page_element(self.WOMAN_TOPS_PAGE)
        woman_tops_bras_element = self.find_page_element(self.WOMAN_TOPS_BRA_PAGE)

        self.action_chains().move_to_element(woman_store_element).perform()
        self.action_chains().move_to_element(woman_tops_element).perform()
        self.action_chains().move_to_element(woman_tops_bras_element).click().perform()

    def open_woman_bottoms_page(self):
        woman_store_element = self.driver.find_page_element(self.WOMAN_PAGE)
        woman_bottoms_element = self.driver.find_page_element(self.WOMAN_BOTTOM_PAGE)

        self.action_chains().move_to_element(woman_store_element)
        self.action_chains().move_to_element(woman_bottoms_element).click().perform()

    def open_woman_bottoms_pants(self):
        woman_store_element = self.driver.find_page_element(self.WOMAN_PAGE)
        woman_bottoms_element = self.driver.find_page_element(self.WOMAN_BOTTOM_PAGE)
        woman_bottoms_pants_element = self.driver.find_page_element(self.WOMAN_BOTTOM_PANTS_PAGE)

        self.action_chains().move_to_element(woman_store_element).perform()
        self.action_chains().move_to_element(woman_bottoms_element).perform()
        self.action_chains().move_to_element(woman_bottoms_pants_element).click().perform()

    def open_woman_bottoms_shorts(self):
        woman_store_element = self.driver.find_page_element(self.WOMAN_PAGE)
        woman_bottoms_element = self.driver.find_page_element(self.WOMAN_BOTTOM_PAGE)
        woman_bottoms_shorts_element = self.driver.find_page_element(self.WOMAN_BOTTOM_SHORTS_PAGE)

        self.action_chains().move_to_element(woman_store_element).perform()
        self.action_chains().move_to_element(woman_bottoms_element).perform()
        self.action_chains().move_to_element(woman_bottoms_shorts_element).click().perform()

    # def open_bottoms_shorts(self):
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(self.woman_store_element).perform()
    #     actions.move_to_element(self.woman_bottoms_element).perform()
    #     actions.move_to_element(self.woman_bottoms_shorts_element).click().perform()

    def product_cards_are_present(self):
        return len(self.find_page_elements(self.PRODUCT_CARDS_LIST))




