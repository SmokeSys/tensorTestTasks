from .locators import PicPageLocators
from .main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PicPage(MainPage): 
    def should_be_pic_href(self):
        assert self.browser.find_element(*PicPageLocators.PICTURES), "На этой странице картинок нет!"

    #Кликает на категорию и проверяет наличие соответствующего текста в searchbar'e
    def pic_click_to(self, how, where): 
        click_item = self.browser.find_element(how, where)  
        click_item_text = click_item.get_attribute("data-grid-text")    #достаем соответствующий категории текст
        click_href = self.browser.find_element(how, where + " a")   #поиск кнопки внутри элемента
        click_href.click()  
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((PicPageLocators.SEARCHTEXT))    #Ждем прогрузку страницы
            ) 
        WebDriverWait(self.browser, 10).until_not(EC.title_contains("Яндекс.Картинки:"))    #Ждем прогрузку картинок
        next_text = self.browser.title.split(':')[0]    #Не смог достать из search bar'a текст :(
        assert next_text == click_item_text, "Текст в search bar'е другой" 
       
    #Открывает картинку
    def pic_open(self, how, where):
        click_pic = self.browser.find_element(how, where).click()
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((PicPageLocators.ISPICOPENED))) #Ждет пока картинка откроется

    #Меняет картинки
    def switch_pic(self, where):
        click_to = self.browser.find_elements(*PicPageLocators.CIRCLEBUTTON)[where] #Выбирает нужную кнопку
        current_img_src = self.browser.find_element(*PicPageLocators.PICSRC).get_attribute("src")
        click_to.click()
        return current_img_src  #возвращает ссылку на источник картинки

    #Возвращает ссылку на источник картинки
    def return_src(self):
        return self.browser.find_element(*PicPageLocators.PICSRC).get_attribute("src")

    #Сравнивает источники картинок
    def pic_equal(self, pic_src2):
        if (self.return_src() == pic_src2): return True
        return False


    

            
