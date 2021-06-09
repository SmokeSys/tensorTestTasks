from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.start_url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        try:
            self.browser.get(self.start_url)
        except Exception as e: #badurl
            print(e)

    def change_url(self, url):
        self.browser.current_url = url

    def is_element_present(self, how, what):
        try:
            self.find_element(how, what)
        except NoSuchElementException:
            return False
        return True  
    
    def is_element_displayed(self, how, what):
        try:
            element = self.find_element(how, what)
            if element.is_displayed: return True
        except Exception as e:
            print(e) 
            return False

    def is_element_enabled(self, how, what):
        try:
            element = self.find_element(how, what)
            if element.is_enabled: return True
        except Exception as e:
            print(e) 
            return False

    def is_url_contains(self, partUrl):
        if partUrl in self.browser.current_url: 
            return True
        return False

    def is_url_equal(self, url):
        if url != self.browser.current_url: return False
        return True

    def contains_element(self, where, what):
        try:
            element = self.find_element(where)
            if what in where: return True
        except  Exception as e:
            print(e)
            return False
        finally: return False
    
    def click_to(self, how, where):
        try:
            self.browser.find_element(how, where).click()
        except Exception as e: #notclickable
            print(e)

    def switch_window(self):
        try:
            self.browser.switch_to.window(self.browser.window_handles[1]) #не очень универсально :\
        except Exception as e:
            print(e)
    