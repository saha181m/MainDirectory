from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest as pt
import allure
from allure_commons.types import AttachmentType
from pathlib import Path
from time import sleep, strftime


@pt.fixture
def browser_data():
    browser = webdriver.Chrome()
    browser.maximize_window()
    URL = 'https://www.dvddom.ru/'
    browser.get(URL)
    yield browser
    browser.close()
@pt.fixture
def act(browser_data:webdriver.Chrome):
    actions=ActionChains(browser_data)
    return actions

@pt.fixture
def get_screenshot(browser_data:webdriver.Chrome):
    screen_dir = Path('screenshots')
    screen_dir.mkdir(exist_ok=True)
    file_name = screen_dir / f'{strftime("%Y-%m-%d_%H_%M_%S")}.png'
    return browser_data.save_screenshot(file_name)



@allure.story("Тест поиска существующего товара Chrome_allure")
@allure.title("Тест поиска существующего товара Chrome_allure")
def test_search(browser_data:webdriver.Chrome, act:ActionChains):
    with allure.step('Поиск наименования фильма'):
        search=browser_data.find_element(By.XPATH,"/html/body/header/nav[3]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/input")
        search.send_keys('Дэдпул')
    with allure.step('Нажатие на кнопку "Найти"'):
        find_button=browser_data.find_element(By.XPATH,"/html/body/header/nav[3]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div")
        act.move_to_element(find_button)
        act.click()
        act.perform()
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='search',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Chrome_allure/search.png')
    assert 'дэдпул — DVD DOM интернет-магазин DVD и Blu-Ray дисков. Купить лицензионные фильмы на двд и блюрей' in browser_data.title
    with allure.step('Кликаем по логотипу'):
        logo = browser_data.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div/div[1]/a/img")
        logo.click()
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='search1',
                      attachment_type=AttachmentType.PNG)
        # browser_data.save_screenshot('/Diplom/Chrome_allure/search1.png')
    with allure.step('Нажатие категорий'):
        proverka = WebDriverWait(browser_data, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/div/section[1]/h5/a"))).text
        assert "Новинки DVD" == proverka
        name_menu = ['Новинки', 'Последние', 'DVD', 'Blu-Ray', 'Предзаказ', 'CD Music']
        proverka_name = []
        for element_name in name_menu:
            locator = (By.XPATH, f"//div[contains(@class,'category')]//*[text()='{element_name}']")

            try:
                element = WebDriverWait(browser_data, 10).until(EC.element_to_be_clickable(locator))
                element.click()
                proverka_name.append(element_name)
                # browser_data.save_screenshot('/Diplom/Chrome_allure/search2.png')
            except Exception as e:
                print(f"Не удалось выполнить клик по элементу '{element_name}': {e}")
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='search2',
                        attachment_type=AttachmentType.PNG)
    print(proverka_name)
    assert proverka_name == ['Новинки', 'Последние', 'DVD', 'Blu-Ray', 'Предзаказ', 'CD Music']


if __name__=='__main__':
    pt.main()
