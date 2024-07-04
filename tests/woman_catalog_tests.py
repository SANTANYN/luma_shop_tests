import time

from base.base_test import BaseTest


class TestsWomanCatalog(BaseTest):

    def test_12_product_cards_on_page(self):
        self.HomePage.open_home_page()
        self.WomanCatalogPage.open_woman_tops_jacket_page()

        assert self.WomanCatalogPage.product_cards_are_present() > 0, "No product cards found on the jackets page"
        assert self.WomanCatalogPage.product_cards_are_present() == 12, "it is not a 12 product cards on the page"

    def test_product_card_are_exist(self):
        self.HomePage.open_home_page()
        # self.WomanCatalogPage.open_bottoms_shorts()

        assert self.WomanCatalogPage.product_cards_are_present() > 0, "No product cards found on the jackets page"
        assert self.WomanCatalogPage.product_cards_are_present() == 12, "it is not a 12 product cards on the page"

