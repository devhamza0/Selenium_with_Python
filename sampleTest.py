from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_first_Component():

    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    password_box = driver.find_element(by=By.NAME, value="my-password")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    password_box.send_keys("1234")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()


def drive_Load():
    option = Options()
    option.page_load_strategy = "normal" #8.539 sec
    # option.page_load_strategy = "eager" #8.744 sec
    # option.page_load_strategy = "none" #7.413 sec
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.quit()


def main():
    # test_first_Component()
    drive_Load()


if __name__ == "__main__":
    main()
