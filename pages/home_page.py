from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class HomePage(BasePage):
    WOMEN_CLOTHES_PAGE = ("id", "ui-id-4")
    TOPS_MENU = (By.ID, "ui-id-9")
    JACKETS_MENU = (By.ID, "ui-id-12")
