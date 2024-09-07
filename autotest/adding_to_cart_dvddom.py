from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest as pt


@pt.fixture
def browser_data():
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = "yandexdriver.exe"
    service = webdriver.ChromeService(executable_path=binary_yandex_driver_file)
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    URL = 'https://www.dvddom.ru/'
    browser.get(URL)
    yield browser
    browser.close()
@pt.fixture
def act(browser_data:webdriver.Chrome):
    actions=ActionChains(browser_data)
    return actions

def test_add_cart(browser_data:webdriver.Chrome,act:ActionChains):
    menu = browser_data.find_element(By.XPATH, '/html/body/main/div/div/nav/div[1]/div/div[2]/ul/li[1]/a')
    act.move_to_element(menu)
    act.perform()
    browser_data.save_screenshot('/Diplom/Yandex/adding_to_cart1.png')
    menu_cat = browser_data.find_element(By.XPATH,'/html/body/main/div/div/nav/div[1]/div/div[2]/ul/li[1]/ul/li[2]/a')
    act.move_to_element(menu_cat)
    act.click()
    act.perform()
    sleep(2)
    product=browser_data.find_element(By.CSS_SELECTOR,'#product-list > ul.product-list.expandable.colored.thumbs > li:nth-child(2) > div')
    act.move_to_element(product)
    act.click()
    act.perform()
    sleep(2)
    browser_data.save_screenshot('/Diplom/Yandex/adding_to_cart2.png')
    quantity=browser_data.find_element(By.CSS_SELECTOR,'#cart-form > div.purchase > div > div.added2cart_block > div.added2cart_sub_block > div.qty-wrapper > input[type=text]')
    act.move_to_element(quantity)
    act.double_click()
    act.perform()
    quantity.send_keys('5')
    sleep(5)
    browser_data.save_screenshot('/Diplom/Yandex/adding_to_cart3.png')
    product_add_cart=browser_data.find_element(By.CLASS_NAME,'second-type')
    act.move_to_element(product_add_cart)
    act.click()
    act.perform()
    sleep(2)
    cart_info=browser_data.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div/div[4]/a/i')
    act.move_to_element(cart_info)
    act.click()
    act.perform()
    sleep(5)
    browser_data.save_screenshot('/Diplom/Yandex/adding_to_cart4.png')
    content=browser_data.find_element(By.CSS_SELECTOR,'body > main')
    print(content.text)
    assert 'Смерч 2*' in content.text
    inp=content.find_element(By.CLASS_NAME,'qty')
    assert inp.get_attribute('value')=='5'

if __name__=='__main__':
    pt.main()