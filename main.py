import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait





driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

url = "enter website url"
driver.get(url)

news_article = driver.find_elements((By.TAG_NAME, "article"))

data = []

for post in news_article:
    try:
        title = post.find_element(By.TAG_NAME, "enter tag").text
        link = post.find_element(By.TAG_NAME, "a").get_attribute("href")

        data.append([title, link])

    except Exception as e:
        print(f"An error occured: {e}")


with open("news_acrticle.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    writer.writerows(data)



driver.quit()

print("Scaping complete! Data saved to news_articles.csv")