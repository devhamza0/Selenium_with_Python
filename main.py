# Automating Amazon
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&ref=nav_em__nav_desktop_sa_intl_computer_accessories_and_peripherals_0_2_6_2")

elem_list = browser.find_element(
    by=By.CSS_SELECTOR, value="div.s-main-slot.s-result-list.s-search-results.sg-row")

items = elem_list.find_elements(
    by=By.XPATH, value='//div[@data-component-type="s-search-result"]')

print(len(items))

for item in items:
    title = item.find_element(by=By.TAG_NAME, value="h2").text
    price = "No Price Found"
    img = "Image not Found"
    link = item.find_element(
        by=By.CLASS_NAME, value="a-link-normal").get_attribute('href')

    try:
        price = item.find_element(
            by=By.CLASS_NAME, value="a-price").text.replace("\n", ".")
    except:
        pass

    try:
        img = item.find_element(
            by=By.CSS_SELECTOR, value=".s-image").get_attribute("src")
    except:
        pass

    print("Title: " + title)
    print("Price:" + price)
    print("Image:" + img)
    print("Link:" + link + "\n")

# def testAmazon():
#     browser = webdriver.Chrome()
#     browser.get("https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&ref=nav_em__nav_desktop_sa_intl_computer_accessories_and_peripherals_0_2_6_2")

#     elem_list = browser.find_element(
#         by=By.CSS_SELECTOR, value="div.s-main-slot.s-result-list.s-search-results.sg-row")

#     items = elem_list.find_element(
#         by=By.XPATH, value='//div[@data-component-type="s-search-result"]')

#     for item in items:
#         title = item.find_element(by=By.TAG_NAME, value="h2").text
#         print("Title: " + title)


# def main():
#     testAmazon()


# if __name__ == "__main__":
#     main()
