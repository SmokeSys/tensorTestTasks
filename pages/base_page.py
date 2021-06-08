from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.find_element(how, what)
        except NoSuchElementException:
            return False
        return True  
    
    def is_element_enabled(self, how, what):
        try:
            element = self.find_element(how, what)
            if element.is_enabled: return True
        except Exception as e:
            print(e) 
            return False

    def is_url_equal(self, url):
        if url != self.url: return False
        return True

    def contains(self, where, what):
        try:
            element = self.find_element(where)
            if what in where: return True
        except  Exception as e:
            print(e)
            return False
        finally: return False
    