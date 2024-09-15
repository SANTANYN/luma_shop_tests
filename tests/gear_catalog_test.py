import allure
import pytest

from base.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@allure.feature("gear catalog page tests")
class TestGearCatalog(BaseTest):

    @allure.severity("Critical")
    @allure.title("check that we can navigate to gear bags catalog page, and prices are present")
    def test_navigate_to_gear_bags_page_and_get_price(self):
        self.home_page.open_home_page()
        self.home_page.is_opened()
        self.gear_catalog_page.open_gear_bags_page()
        self.gear_catalog_page.open_gear_bags_page()
        prices = self.gear_catalog_page.get_products_prices()
        prices_without_dollar = [price.replace('$', '') for price in prices]
        assert prices_without_dollar != []

