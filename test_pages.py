from .pages.locators import TestPageLocators
from .pages.main_page import MainPage
from .pages.pic_page import PicPage
import pytest
 
@pytest.mark.test1
@pytest.mark.xfail(reason="Not all links contain tensor.ru")
def test_search_page(browser):
    mpage = MainPage(browser, TestPageLocators.LINK)
    mpage.open()
    mpage.should_be_search_bar()
    mpage.write_to_searchbar("Тензор")
    assert mpage.is_suggest_is_displayed() == True, "Подсказки не отображены"
    mpage.send_enter_to_search()
    mpage = mpage.go_to_url(browser.current_url)
    mpage.check_contain_in_result("tensor.ru")
        

@pytest.mark.test2
#@pytest.mark.xfail
def test_pic_page(browser):
    ppage = PicPage(browser, TestPageLocators.LINK)
    ppage.open()
    ppage.should_be_pic_href()
    ppage.click_to(*TestPageLocators.PICTURES)
    ppage.switch_window()
    ppage.is_url_contains(TestPageLocators.PICLINK) 
    ppage.pic_click_to(*TestPageLocators.PICTURETOCLICKONMAINPAGE) 
    ppage.pic_open(*TestPageLocators.PICTURETOCLICKONSECONDARYPAGE)    
    #pic_first_src = ppage.switch_pic(-1) #Иногда Я.Картинка содержит ссылку на оригинальный источник, а не на яндекс :\
    #pic_first_src = ppage.switch_pic(0)  #Но при переключении все фиксится :)    
    pic_first_src = ppage.switch_pic(-1)    # -1 next, 0 back
    assert ppage.pic_equal(pic_first_src) == False, "Картинка не сменилась\nimgsrc:\nOrig:{pic_first_src}\nCurr:{ppage.return_src()} "
    ppage.switch_pic(0)
    assert ppage.pic_equal(pic_first_src) == True, f"Картинка не совпадает с первоначальной\nimgsrc:\nOrig:{pic_first_src}\nCurr:{ppage.return_src()}"
    


