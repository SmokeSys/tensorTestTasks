from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage): 
    def should_be_search_bar(self):
        assert self.browser.find_element(*MainPageLocators.SEARCH), "Search bar doesnt exist"
    
    def go_to_url(self, url):
        return MainPage(self.browser, url)
            
    def write_to_searchbar(self, text):
        self.browser.find_element(*MainPageLocators.SEARCH).send_keys(text)

    def is_suggest_is_enabled(self):
        assert self.browser.find_element(*MainPageLocators.SUGGEST).is_enabled, "Suggest not enabled"

    def send_enter_to_search(self):
        self.browser.find_element(*MainPageLocators.SEARCH).send_keys(Keys.ENTER)
    
    def check_contain_in_result(self, what):
        results = self.browser.find_elements(*MainPageLocators.SEARCH_RESULT_HREF)
        for result in results:
            assert what in result.get_attribute("href"), f"Ссылка не содержит {what}"
    

            
