import time
import allure
import pytest

from base.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@allure.feature("woman catalogs pages tests")
class TestWomenCatalog(BaseTest):

    @allure.severity("Critical")
    @pytest.mark.smoke
    @allure.title("check that we can navigate to women catalog page, and its exactly main woman catalog page")
    def test_navigate_to_women_page(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_store_page()
        title = self.women_catalog_page.get_page_title("Women")
        assert title.text == "Women"

    @allure.severity("Critical")
    @pytest.mark.smoke
    @allure.title("check that in the hot sellers block product cards are present")
    def test_check_hot_sellers_items(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_store_page()
        sellers_list = self.women_catalog_page.product_cards_are_present_in_hot_sellers_list()
        assert sellers_list == 4

    @allure.severity("Critical")
    @pytest.mark.smoke
    @allure.title("check that in the catalog page exactly 12 cards in catalog")
    def test_12_product_cards_on_page(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.get_women_store_tops_page_element()

        assert self.women_catalog_page.product_cards_are_present() > 0, "No product cards found on the jackets page"
        assert self.women_catalog_page.product_cards_are_present() == 12, "it is not a 12 product cards on the page"

    @allure.severity("Critical")
    @pytest.mark.smoke
    @allure.title("check that in bottoms short catalog page product cards are present")
    def test_product_card_are_present_in_bottom_shorts(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_bottoms_shorts()

        assert self.women_catalog_page.product_cards_are_present() > 0, "No product cards found on the jackets page"
        assert self.women_catalog_page.product_cards_are_present() == 12, "it is not a 12 product cards on the page"
