from .pages.locators import TestPageLocators
from .pages.main_page import MainPage
import pytest
 

@pytest.mark.test1
def test_search_page(browser):
    mpage = MainPage(browser, TestPageLocators.LINK)
    mpage.open()
    mpage.should_be_search_bar()
    mpage.write_to_searchbar("Тензор")
    mpage.is_suggest_is_enabled()
    mpage.send_enter_to_search()
    mpage = mpage.go_to_url(browser.current_url)
    mpage.check_contain_in_result("tensor.ru")
        


@pytest.mark.test2
@pytest.mark.skip
def test_pic_page(browser):
    mpage = MainPage(browser, TestPageLocators.LINK)
    mpage.Open()