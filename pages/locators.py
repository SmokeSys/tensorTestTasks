from selenium.webdriver.common.by import By

class MainPageLocators:
    SEARCH = (By.CSS_SELECTOR, "#text")
    SUGGEST = (By.CSS_SELECTOR, "ul.mini-suggest__popup-content") #только после введения слова в поиске
    SEARCH_RESULT_HREF = (By.CSS_SELECTOR, "#search-result[role=\"main\"]>[data-cid] h2 > .Link[href]")

class TestPageLocators:
    LINK = "https://yandex.ru/"