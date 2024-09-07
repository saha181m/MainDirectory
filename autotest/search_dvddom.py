from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest as pt



@pt.fixture
def browser_data():
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = "yandexdriver.exe"
    service = webdriver.ChromeService(executable_path=binary_yandex_driver_file)
    browser = webdriver.Chrome(service=service,options = options)
    browser.maximize_window()
    URL = 'https://www.dvddom.ru/'
    browser.get(URL)
    yield browser
    browser.close()
@pt.fixture
def act(browser_data:webdriver.Chrome):
    actions=ActionChains(browser_data)
    return actions


def test_search(browser_data:webdriver.Chrome, act:ActionChains):
    search=browser_data.find_element(By.XPATH,"/html/body/header/nav[3]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/input")
    search.send_keys('Дэдпул')
    find_button=browser_data.find_element(By.XPATH,"/html/body/header/nav[3]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div")
    act.move_to_element(find_button)
    act.click()
    act.perform()
    sleep(3)
    browser_data.save_screenshot('/Diplom/Yandex/search.png')
    assert 'дэдпул — DVD DOM интернет-магазин DVD и Blu-Ray дисков. Купить лицензионные фильмы на двд и блюрей' in browser_data.title
    logo = browser_data.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div/div[1]/a/img")

    logo.click()
    browser_data.save_screenshot('/Diplom/Yandex/search1.png')
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
            browser_data.save_screenshot('/Diplom/Yandex/search2.png')
        except Exception as e:
            print(f"Не удалось выполнить клик по элементу '{element_name}': {e}")
    print(proverka_name)
    assert proverka_name == ['Новинки', 'Последние', 'DVD', 'Blu-Ray', 'Предзаказ', 'CD Music']


if __name__=='__main__':
    pt.main()
