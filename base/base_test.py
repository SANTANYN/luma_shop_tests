from pages.home_page import HomePage
from pages.women_catalog_page import WomenCatalogPage
from config.data import Data
from config.links import Links
import pytest


class BaseTest:
    Data: Data
    Links: Links

    home_page: HomePage
    women_catalog_page: WomenCatalogPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.home_page = HomePage(driver)
        request.cls.women_catalog_page = WomenCatalogPage(driver)
