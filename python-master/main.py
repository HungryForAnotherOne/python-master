from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os

# options
from settings import CHROME_PATH


options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--kiosk")
p = "Test{}".format(random.randint(1, 255))
# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

driver = webdriver.Chrome(
    executable_path=CHROME_PATH,
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("http://91.242.35.147/security/authenticate")
    time.sleep(3)

    email_input = driver.find_element_by_xpath("//input[@type='text']")
    email_input.clear()
    email_input.send_keys("hiARTER")
    time.sleep(1)

    password_input = driver.find_element_by_xpath("//input[@type='password']")
    password_input.clear()
    password_input.send_keys("hiARTER1")
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)
    time.sleep(4)

    driver.get("http://91.242.35.147/promotions")
    time.sleep(3)

    task_button = driver.find_element_by_xpath("//button['@id=main-scroll]/div/div[1]/button']").click()
    time.sleep(3)

    driver.find_element_by_xpath(
        "//div[@class = 'cs-selector__placeholder' and text() = '" 'Группа товара'  "']").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//div[@class = 'cs-selector__placeholder' and text() = '" 'Группа товара'
        "']/../../following-sibling::div//span[text()='" 'Обувь' "']").click()
    time.sleep(3)

    text_input = driver.find_element_by_xpath(
        "//textarea[@class = 'textarea__input textarea__input sbs-task__item-textarea']")
    text_input.send_keys(p)
    time.sleep(3)

    texti_input = driver.find_element_by_xpath(
        "//textarea[@class = 'textarea__input promotions_block-textarea']")
    texti_input.send_keys(p)
    time.sleep(3)

    driver.find_element_by_xpath(
        "//div[@class = 'cs-selector__placeholder' and text() = '" 'Изображение'  "']").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//div[@class ='cs-selector__list cs-selector__list_size-w-by-field cs-selector__"
        "list_position-right cs-selector__list_open']/div/span[2]").click()
    time.sleep(3)

    texti_input = driver.find_element_by_xpath(
        "//textarea[@class = 'textarea__input sbs-info__item-textarea']")
    texti_input.send_keys(p)
    time.sleep(3)

    driver.find_element_by_xpath(
        "//div[@class = 'cs-selector__placeholder' and text() = '" 'Действие'  "']").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//div[@class = 'cs-selector__placeholder' and text() = '" 'Действие'
        "']/../../following-sibling::div//span[text()='" 'Отметка на карте' "']").click()
    time.sleep(3)

    driver.find_element_by_xpath(
        "//div[@class = 'cs-selector__placeholder' and text() = '" 'Вид нарушения'  "']").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//div[@class = 'cs-selector__placeholder' and text() = '" 'Вид нарушения'
        "']/../../following-sibling::div//span[text()='" 'Подозрительно низкая цена' "']").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//div[@class = 'cs-selector__placeholder' and text() = '" 'Вид нарушения'  "']").click()

    texts_input = driver.find_element_by_xpath(
        "//textarea[@class = 'textarea__input sbs-task__item-textarea']")
    texts_input.send_keys(p)
    time.sleep(3)

    driver.find_element_by_xpath(
        "//div[@class = 'two-column-buttons']/button[2]").click()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
