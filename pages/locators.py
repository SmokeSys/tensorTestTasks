from selenium.webdriver.common.by import By

class MainPageLocators:
    SEARCH = (By.CSS_SELECTOR, ".input__control[name=\"text\"]")
    SUGGEST = (By.CSS_SELECTOR, ".body_search_yes")
    SEARCHRESULTHREF = (By.CSS_SELECTOR, "#search-result[role=\"main\"]>[data-cid] h2 > .Link[href]")
    PICTURES = (By.CSS_SELECTOR, "[data-id=\"images\"]")

class TestPageLocators:
    LINK = "https://yandex.ru/" 
    PICTURES = (By.CSS_SELECTOR, "[data-id=\"images\"]")
    PICLINK = "https://yandex.ru/images/"
    PICTURETOCLICKONMAINPAGE = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")
    PICTURETOCLICKONSECONDARYPAGE = (By.CSS_SELECTOR, "a.serp-item__link")

class PicPageLocators:
    SEARCHTEXT = (By.CSS_SELECTOR, "[name=\"description\"]")
    PICTURES = (By.CSS_SELECTOR, "[data-id=\"images\"]")
    ISPICOPENED = (By.CSS_SELECTOR, ".Popup2.Popup2_visible")
    CIRCLEBUTTON = (By.CSS_SELECTOR, ".CircleButton")
    PICSRC = (By.CSS_SELECTOR, "img.MMImage-Origin")
    