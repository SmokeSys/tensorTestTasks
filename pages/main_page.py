from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage): 
    def should_be_search_bar(self):
        assert self.browser.find_element(*MainPageLocators.SEARCH), "Search bar doesnt exist"
    
    def go_to_url(self, url):
        return MainPage(self.browser, url)
            
    def write_to_searchbar(self, text):
        self.browser.find_element(*MainPageLocators.SEARCH).send_keys(text)

    def is_suggest_is_enabled(self):
        try: 
            self.browser.find_element(*MainPageLocators.SUGGEST)
            return True
        except NoSuchElementException: 
            print("Suggest not active or doesnt exist")
            return False

    def is_suggest_is_displayed(self):
        try: 
            el = self.browser.find_element(*MainPageLocators.SUGGEST)
            if el.is_displayed:
                return True
            return False
        except NoSuchElementException: 
            print("Suggest not active or doesnt exist")
            return False

    def send_enter_to_search(self):
        self.browser.find_element(*MainPageLocators.SEARCH).send_keys(Keys.ENTER)
    
    #Проверяет наличие строки в ссылке
    def check_contain_in_result(self, what):
        results = self.browser.find_elements(*MainPageLocators.SEARCHRESULTHREF)
        i = 0        
        for result in results:
            if i == 5: break
            assert what in result.get_attribute("href"), f"Не все ссылки содержат {what}"
            i += 1



    

            
