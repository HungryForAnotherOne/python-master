from selenium.webdriver.chrome.webdriver import WebDriver


def select_value_in_div_dropdown(driver: WebDriver, drop_down_value: str):
    driver.find_element_by_xpath(
        "//div[@class = 'cs-selector__placeholder' and text() = '" 'Группа товара'  "']").click()
    driver.find_element_by_xpath(
        "//div[@class = 'cs-selector__placeholder' and text() = '" 'Группа товара' 
        "']/../../following-sibling::div//span[text()='" + drop_down_value + "']").click()
