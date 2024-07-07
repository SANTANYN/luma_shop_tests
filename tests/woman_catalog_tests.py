import time

import pytest

from base.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestsWomanCatalog(BaseTest):

    def test_12_product_cards_on_page(self):
        self.home_page.open_home_page()
        self.woman_catalog_page.open_woman_tops_jacket_page()

        assert self.woman_catalog_page.product_cards_are_present() > 0, "No product cards found on the jackets page"
        assert self.woman_catalog_page.product_cards_are_present() == 12, "it is not a 12 product cards on the page"

    def test_product_card_are_exist(self):
        self.home_page.open_home_page()
        self.woman_catalog_page.open_woman_bottoms_shorts()

        assert self.woman_catalog_page.product_cards_are_present() > 0, "No product cards found on the jackets page"
        assert self.woman_catalog_page.product_cards_are_present() == 12, "it is not a 12 product cards on the page"

