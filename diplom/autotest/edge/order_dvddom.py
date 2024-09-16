from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest as pt
from selenium.webdriver.support.ui import Select
import allure
from allure_commons.types import AttachmentType
from pathlib import Path
from time import sleep, strftime



@pt.fixture
def browser_data():
    browser = webdriver.Edge()
    browser.maximize_window()
    URL = 'https://www.dvddom.ru/'
    browser.get(URL)
    yield browser
    browser.close()
@pt.fixture
def act(browser_data:webdriver.Edge):
    actions=ActionChains(browser_data)
    return actions

@pt.fixture
def get_screenshot(browser_data:webdriver.Edge):
    screen_dir = Path('screenshots')
    screen_dir.mkdir(exist_ok=True)
    file_name = screen_dir / f'{strftime("%Y-%m-%d_%H_%M_%S")}.png'
    return browser_data.save_screenshot(file_name)

@allure.story("Тест оформления заказа Edge_allure")
@allure.title("Тест оформления заказа Edge_allure")
def test_order(browser_data:webdriver.Edge, act:ActionChains):
    with allure.step('Авторизация на сайте'):
        signin=browser_data.find_element(By.XPATH,"/html/body/header/div[1]/div/div/div/div[3]/ul/li/a[1]")
        act.move_to_element(signin)
        act.click()
        act.perform()
        sleep(5)
        email=browser_data.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/input")
        act.move_to_element(email)
        act.click()
        act.perform()
        email.send_keys('amvrosi61@example.net')
        password=browser_data.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/input")
        act.move_to_element(password)
        act.click()
        act.perform()
        password.send_keys('j1WWR)b5#o')
        button=browser_data.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[3]/div[2]/input[2]")
        act.move_to_element(button)
        act.click()
        act.perform()
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='order1',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Edge_allure/order1.png')
    sleep(5)
    with allure.step('Выбор товара'):
        product=browser_data.find_element(By.XPATH,'/html/body/main/div/div/div/section[1]/ul/li[4]/div/div[1]/a/div/div[2]')
        act.move_to_element(product)
        act.click()
        act.perform()
        sleep(10)
        add_product=browser_data.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/div/div[2]/form/div[4]/div/div[2]/div[1]/div[2]/input')
        act.move_to_element(add_product)
        act.click()
        act.perform()
    sleep(5)
    with allure.step('Переход в корзину'):
        trash=browser_data.find_element(By.XPATH,'/html/body/header/div[1]/div/div/div/div[4]/a')
        act.move_to_element(trash)
        act.click()
        act.perform()
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='order2',
                          attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Edge_allure/order2.png')
    sleep(5)
    with allure.step('Нажатие на кнопку "Оформить заказ"'):
        order=browser_data.find_element(By.XPATH,'/html/body/main/div/div/div/form/div[1]/div[5]/div[2]/input')
        act.move_to_element(order)
        act.click()
        act.perform()
        sleep(5)
    with allure.step('Заполнение формы "Контактная информация"'):
        order_name=browser_data.find_element(By.XPATH,'/html/body/main/div/div/div/div/div[1]/form/div[2]/div[1]/div/div/div[1]/div[2]/input')
        act.move_to_element(order_name)
        act.double_click()
        act.perform()
        order_name.send_keys('Ярослав')
        sleep(5)
        order_last_name=browser_data.find_element(By.XPATH,'/html/body/main/div/div/div/div/div[1]/form/div[2]/div[1]/div/div/div[2]/div[2]/input')
        act.move_to_element(order_last_name)
        act.double_click()
        act.perform()
        order_last_name.send_keys('Иванов')
        sleep(2)
        order_phone=browser_data.find_element(By.NAME,'customer[phone]')
        act.move_to_element(order_last_name)
        act.click()
        act.perform()
        order_phone.send_keys('9183265153')
        sleep(5)
        order_region=Select(browser_data.find_element(By.XPATH,'/html/body/main/div/div/div/div/div[1]/form/div[2]/div[1]/div/div/div[5]/div[2]/p/span[2]/select'))
        order_region.select_by_value("77")
        sleep(5)
        order_city=browser_data.find_element(By.NAME,'customer[address.shipping][city]')
        act.move_to_element(order_city)
        act.double_click()
        act.perform()
        order_city.send_keys('Москва')
        order_street = browser_data.find_element(By.NAME,'customer[address.shipping][street]')
        act.move_to_element(order_street)
        act.double_click()
        act.perform()
        order_street.send_keys('Бирюлевская')
        order_num_house=browser_data.find_element(By.NAME,'customer[address.shipping][dom]')
        act.move_to_element(order_num_house)
        act.double_click()
        act.perform()
        order_num_house.send_keys('5')
        order_index=browser_data.find_element(By.NAME,'customer[address.shipping][zip]')
        act.move_to_element(order_index)
        act.double_click()
        act.perform()
        order_index.send_keys('123000')
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='order3',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Edge_allure/order3.png')
    with allure.step('Нажатие на кнопку "Далее"'):
        order_button=browser_data.find_element(By.XPATH,'/html/body/main/div/div/div/div/div[1]/form/div[2]/input[2]')
        act.move_to_element(order_button)
        act.click()
        act.perform()
        order_button_cont=browser_data.find_element(By.XPATH,'/html/body/main/div/div/div/div/div[1]/form/div[2]/input[2]')
        act.move_to_element(order_button_cont)
        act.click()
        act.perform()
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='order4',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Edge_allure/order4.png')
    sleep(5)
    with allure.step('Выбор чекбокса в разделе "Доставка"'):
        checkbox = browser_data.find_element(By.CSS_SELECTOR,'#page-content > div > div.checkout-step.step-shipping > form > div > div.checkout-content > ul > li.shipping-34 > h3 > label > span.at-stylize-box')
        act.move_to_element(checkbox)
        act.click()
        act.perform()
        order_cont = browser_data.find_element(By.CSS_SELECTOR, '#page-content > div > div.checkout-step.step-shipping > form > div > input[type=submit]:nth-child(4)')
        act.move_to_element(order_cont)
        act.click()
        act.perform()
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='order5',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Edge_allure/order5.png')
    sleep(5)
    with allure.step('Выбор чекбокса в разделе "Оплата"'):
        checkbox2 = browser_data.find_element(By.XPATH,'/html/body/main/div/div/div/div/div[3]/form/div/div[1]/ul/li[2]/h3/label/span[1]')
        act.move_to_element(checkbox2)
        act.click()
        act.perform()
        with allure.step('Делаем скриншот'):
            allure.attach(browser_data.get_screenshot_as_png(), name='order6',
                          attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Edge_allure/order6.png')
    sleep(5)
    order_button_pay=browser_data.find_element(By.CSS_SELECTOR,'#page-content > div > div.checkout-step.step-payment > form > div > input[type=submit]:nth-child(4)')
    act.move_to_element(order_button_pay)
    act.click()
    act.perform()
    sleep(5)
    with allure.step('Подтверждение заказа'):
        order_button_final=browser_data.find_element(By.XPATH,'/html/body/main/div/div/div/div/div[4]/form/div/div[3]/input')
        act.move_to_element(order_button_final)
        act.click()
        act.perform()
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='order7',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Edge_allure/order7.png')
    sleep(10)
    proverka = WebDriverWait(browser_data, 5).until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text
    assert 'Спасибо!'==proverka

if __name__=='__main__':
    pt.main()
