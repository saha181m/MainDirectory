from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest as pt
import allure
from allure_commons.types import AttachmentType
from pathlib import Path
from time import sleep, strftime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pt.fixture
def browser_data():
    browser = webdriver.Firefox()
    browser.maximize_window()
    URL = 'https://www.dvddom.ru/'
    browser.get(URL)
    yield browser
    browser.close()

@pt.fixture
def act(browser_data:webdriver.Firefox):
    actions=ActionChains(browser_data)
    return actions

@pt.fixture
def get_screenshot(browser_data:webdriver.Firefox):
    screen_dir = Path('screenshots')
    screen_dir.mkdir(exist_ok=True)
    file_name = screen_dir / f'{strftime("%Y-%m-%d_%H_%M_%S")}.png'
    return browser_data.save_screenshot(file_name)

@allure.story("Добавление заказа в корзину Firefox_allure")
@allure.title("Добавление заказа в корзину Firefox_allure")
def test_add_cart(browser_data:webdriver.Firefox,act:ActionChains):
    with allure.step('Выбор категории'):
        menu = browser_data.find_element(By.XPATH, '/html/body/main/div/div/nav/div[1]/div/div[2]/ul/li[1]/a')
        act.move_to_element(menu)
        act.perform()
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='adding_to_cart1',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Firefox/adding_to_cart1.png')
    menu_cat = browser_data.find_element(By.XPATH,'/html/body/main/div/div/nav/div[1]/div/div[2]/ul/li[1]/ul/li[2]/a')
    act.move_to_element(menu_cat)
    act.click()
    act.perform()
    sleep(5)
    with allure.step('Выбор товара'):
        product=browser_data.find_element(By.CSS_SELECTOR,'.product-list > li:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2) > img:nth-child(1)')
        act.move_to_element(product)
        act.click()
        act.perform()
    sleep(3)
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='adding_to_cart2',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Firefox/adding_to_cart2.png')
    with allure.step('Изменение количества товара'):
        quantity=browser_data.find_element(By.CSS_SELECTOR,'.qty-wrapper > input:nth-child(2)')
        act.move_to_element(quantity)
        act.double_click()
        act.perform()
        quantity.send_keys('5')
    sleep(5)
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='adding_to_cart3',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Firefox/adding_to_cart3.png')
    with allure.step('Добавление в корзину'):
        product_add_cart=browser_data.find_element(By.CSS_SELECTOR,'div.submit-wrapper:nth-child(2) > input:nth-child(1)')
        act.move_to_element(product_add_cart)
        act.click()
        act.perform()
    sleep(2)
    with allure.step('Переход в корзину'):
        cart_info=browser_data.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div/div[4]/a/i')
        act.move_to_element(cart_info)
        act.click()
        act.perform()
    sleep(5)
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='adding_to_cart4',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Firefox/adding_to_cart4.png')
    content=browser_data.find_element(By.CSS_SELECTOR,'body > main')
    print(content.text)
    proverka = WebDriverWait(browser_data, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > main'))).text
    assert proverka in content.text
    inp=content.find_element(By.CLASS_NAME,'qty')
    assert inp.get_attribute('value')=='5'

if __name__=='__main__':
    pt.main()