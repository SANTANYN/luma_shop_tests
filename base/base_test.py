from pages.home_page import HomePage
from pages.woman_catalog_page import WomanCatalogPage
from config.data import Data
from config.links import Links
import pytest


class BaseTest:
    Data: Data
    Links: Links

    HomePage: HomePage
    WomanCatalogPage: WomanCatalogPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.HomePage = HomePage(driver)
        request.cls.WomanCatalogPage = WomanCatalogPage(driver)


