from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from anticaptchaofficial.imagecaptcha import *
import pytest as pt
import allure
from allure_commons.types import AttachmentType
from pathlib import Path
from time import sleep, strftime


@pt.fixture
def browser_data():
    browser = webdriver.Firefox()
    browser.maximize_window()
    URL = 'https://www.dvddom.ru/'
    browser.get(URL)
    yield browser
    browser.close()
@pt.fixture
def get_screenshot(browser_data:webdriver.Firefox):
    screen_dir = Path('screenshots')
    screen_dir.mkdir(exist_ok=True)
    file_name = screen_dir / f'{strftime("%Y-%m-%d_%H_%M_%S")}.png'
    return browser_data.save_screenshot(file_name)

fake = Faker(locale="ru_RU")
randomName = fake.name()
a = randomName.split()
name = a[0]
last_name = a[1]
phone = fake.phone_number()
randomEmail = fake.email()
randompassword = fake.password()
confirm_password = randompassword


@allure.story("Регистрация на сайте Firefox_allure")
@allure.title("Регистрация на сайте Firefox_allure")
def test_auth(browser_data: webdriver.Firefox):
    with allure.step('Нажатие на кнопку "Регистрация"'):
        auth = browser_data.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div/div[3]/ul/li/a[2]")
        auth.click()
        sleep(5)
    with allure.step('Заполнение формы регистрации'):
        auth_name = browser_data.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/form/section[1]/div[1]/div[2]/input")
        auth_name.send_keys(name)
        sleep(5)
        auth_email = browser_data.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/form/section[1]/div[2]/div[2]/p/input")
        auth_email.send_keys(randomEmail)
        auth_password = browser_data.find_element(By.XPATH,
                                     "/html/body/div[4]/div[2]/div/div[2]/form/section[1]/div[3]/div[2]/input")
        auth_password.send_keys(randompassword)
        print(randomEmail)
        print(randompassword)
        auth_confirm_password = browser_data.find_element(By.XPATH,
                                             "/html/body/div[4]/div[2]/div/div[2]/form/section[1]/div[4]/div[2]/input")
        auth_confirm_password.send_keys(confirm_password)
        capcha_img = browser_data.find_element(By.CLASS_NAME, "wa-captcha-img")
        capcha_img.screenshot("captcha.png")
        apy_key = "b1d8e9ae5f885eac7abd4b04ba9c7416"
        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key(apy_key)
        captcha_text = solver.solve_and_return_solution("captcha.png")
        code = captcha_text
        print(code)
        sleep(15)
        auth_cup = browser_data.find_element(By.CLASS_NAME, "wa-captcha-input")
        auth_cup.send_keys(code)
        sleep(10)
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='auth1',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Firefox/auth1.png')
    with allure.step('Нажатие на кнопку "Регистрация"'):
        button = browser_data.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/section[2]/div[2]/input')
        button.click()
        sleep(5)
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='auth2',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Firefox/auth2.png')
    sleep(2)
    with allure.step('Вход в личный кабинет'):
        reg = browser_data.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div/div[3]/ul/li/a")
        reg.click()
        sleep(2)
    with allure.step('Делаем скриншот'):
        allure.attach(browser_data.get_screenshot_as_png(), name='auth3',
                      attachment_type=AttachmentType.PNG)
    # browser_data.save_screenshot('/Diplom/Firefox/auth3.png')
    proverka = WebDriverWait(browser_data, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/div/div/h1"))).text
    assert "Мои заказы" == proverka

if __name__=='__main__':
    pt.main()
