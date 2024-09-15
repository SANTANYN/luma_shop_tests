import allure
import pytest

from base.base_test import BaseTest
from config.links import PagesLinksForAssertion


@pytest.mark.usefixtures("setup")
@allure.feature("woman catalog page tests")
class TestWomenCatalog(BaseTest):

    @allure.severity("Critical")
    @allure.title("check that we can navigate to women catalog page, and its exactly main woman catalog page")
    def test_navigate_to_women_page(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_store_page()
        title = self.women_catalog_page.get_page_title("Women")
        assert title.text == "Women"

    @allure.severity("Critical")
    @allure.title("Navigate to women catalog page, and check that prises are present in product cards")
    def test_navigate_to_women_page_and_check_that_prices_are_present(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_store_page()
        list_of_prices = self.women_catalog_page.get_products_prices()
        assert list_of_prices != []

    @allure.severity("Critical")
    @allure.title("check that in the hot sellers block product cards are present")
    def test_check_hot_sellers_items(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_store_page()
        sellers_list = self.women_catalog_page.product_cards_are_present_in_hot_sellers_list()
        assert sellers_list == 4

    @allure.severity("Critical")
    @allure.title("check that categories titles are present")
    def test_check_categories_title(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_store_page()
        titles_list = self.women_catalog_page.get_categories_titles()
        assert titles_list == ['TOPS', 'BOTTOMS']

    @allure.severity("Critical")
    @allure.title("check that categories items are present and text is correct")
    def test_categories_items_are_present(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_store_page()
        categories_text_list = self.women_catalog_page.get_categories_items_text()
        assert categories_text_list == ['Tops', 'Bottoms']

    @allure.severity("Critical")
    @allure.title("check that categories links are present and it is correct")
    def test_check_links_for_categories(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_store_page()
        categories_links = self.women_catalog_page.get_main_categories_items_links()
        assert categories_links == PagesLinksForAssertion.WOMEN_PAGE_CATEGORIES_LINKS

    @allure.severity("critical")
    @allure.title("check that items in categories has a correct text and number of items")
    def test_subcategories_menu_items_are_present(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_store_page()
        subcategories_text_list = self.women_catalog_page.get_subcategories_items_text()
        assert subcategories_text_list == ['Hoodies & Sweatshirts', 'Jackets', 'Tees', 'Bras & Tanks', 'Pants',
                                           'Shorts']

    @allure.severity("Critical")
    @allure.title("check that subcategories links are present and it is correct")
    def test_check_links_for_subcategories(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_store_page()
        subcategories_links = self.women_catalog_page.get_subcategories_items_links()
        assert subcategories_links == PagesLinksForAssertion.WOMEN_PAGE_SUBCATEGORIES_LINKS


@pytest.mark.usefixtures("setup")
@allure.feature("woman catalogs tops page tests")
class TestWomenCatalogTopsPage(BaseTest):

    @allure.severity("Critical")
    @allure.title("check that in the catalog page exactly 12 cards in catalog")
    def test_12_product_cards_on_page(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.women_catalog_page.open_women_tops_page()

        assert self.women_catalog_page.product_cards_are_present() > 0, "No product cards found on the jackets page"
        assert self.women_catalog_page.product_cards_are_present() == 12, "it is not a 12 product cards on the page"
