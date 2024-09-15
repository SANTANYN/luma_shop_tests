from pages.home_page import HomePage
from pages.women_catalog_page import WomenCatalogPage
from pages.gear_catalog_page import GearCatalogPage
from config.data import Data
from config.links import Links
import pytest


class BaseTest:
    data: Data
    links: Links

    home_page: HomePage
    women_catalog_page: WomenCatalogPage
    gear_catalog_page: GearCatalogPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.data = Data
        request.cls.links = Links

        request.cls.home_page = HomePage(browser)
        request.cls.women_catalog_page = WomenCatalogPage(browser)
        request.cls.gear_catalog_page = GearCatalogPage(browser)
