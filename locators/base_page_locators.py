from selenium.webdriver.common.by import By


class BasePageLocators:

    # locator for the wats new page
    WATS_NEW_PAGE = (By.ID, "ui-id-3")

    # Locators for the woman section in the main page of store
    WOMAN_STORE_SECTION = ("id", "ui-id-4")
    WOMAN_TOPS_SECTION = (By.ID, "ui-id-9")
    WOMAN_TOPS_JACKETS_SECTION = (By.ID, "ui-id-11")
    WOMAN_TOPS_HOODIES_SECTION = (By.ID, "ui-id-12")
    WOMAN_TOPS_TEES_SECTION = (By.ID, "ui-id-13")
    WOMAN_TOPS_BRA_SECTION = (By.ID, "ui-id-14")
    WOMAN_BOTTOM_SECTION = (By.ID, "ui-id-10")
    WOMAN_BOTTOM_PANTS_SECTION = (By.ID, "ui-id-15")
    WOMAN_BOTTOM_SHORTS_SECTION = (By.ID, "ui-id-16")

    # Locators for the man section in the main paige of store
    MAN_STORE_SECTION = (By.ID, "ui-id-5")
    MAN_TOPS_SECTION = (By.ID, "ui-id-17")
    MAN_TOPS_JACKETS_SECTION = (By.ID, "ui-id-19")
    MAN_TOPS_HOODIES_SECTION = (By.ID, "ui-id-20")
    MAN_TOPS_TEES_SECTION = (By.ID, "ui-id-21")
    MAN_TOPS_TANKS_SECTION = (By.ID, "ui-id-22")
    MAN_BOTTOM_SECTION = (By.ID, "ui-id-18")
    MAN_BOTTOM_PANTS_SECTION = (By.ID, "ui-id-23")
    MAN_BOTTOM_SHORTS_SECTION = (By.ID, "ui-id-24")

    # Locators for the gear section
    GEAR_STORE_SECTION = (By.ID, "ui-id-6")
    GEAR_BAGS_SECTION = (By.ID, "ui-id-25")
    GEAR_FITNESS_SECTION = (By.ID, "ui-id-26")
    GEAR_WATCHES_SECTION = (By.ID, "ui-id-27")

    # Locators for training section
    TRAINING_SECTION = (By.ID, "ui-id-7")
    TRAINING_VIDEO_SECTION = (By.ID, "ui-id-28")

    # Locator for the sale page
    SALE_PAGE = (By.ID, "ui-id-8")

    # Other main page locators
    MAIN_PAGE_SEARCH_INPUT = (By.ID, "search")
    MAIN_PAGE_SHOW_CART = (By.XPATH, "//a[@class='action showcart' and @href]")


# catalog items locator
class CatalogLocators:
    CATALOG_ITEMS_AMOUNT = (By.XPATH, "(//p[@id='toolbar-amount']//span[text()='12'])[1]")
    CATALOG_ITEMS_LIST = (By.XPATH, "//ol")

