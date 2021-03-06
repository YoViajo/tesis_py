## A Selenium scraper for TripAdvisor reviews
## Ref: https://lobeslab.com/a-selenium-scraper-for-tripadvisor-reviews/

import csv
import time
from selenium.webdriver import Chrome

URL = "https://www.tripadvisor.com/Restaurant_Review-g190328-d8867662-Reviews-Storie_Sapori_La_Valletta-Valletta_Island_of_Malta.html"

driver = Chrome("/home/yoviajo/Documentos/chromedriver")
driver.get(URL)

# Prepare CSV file
csvFile = open("reviews.csv", "w", newline='', encoding="utf-8")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['Score','Date','Title','Review'])

# Find and click the More link (to load all reviews)
driver.find_element_by_xpath("//span[@class='taLnk ulBlueLinks']").click()
time.sleep(5) # Wait for reviews to load

reviews = driver.find_elements_by_xpath("//div[@class='ui_column is-9']")
num_page_items = min(len(reviews), 10)

# Loop through the reviews found
for i in range(num_page_items):
    # get the score, date, title and review
    score_class = reviews[i].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class")
    score = score_class.split("_")[3]
    date = reviews[i].find_element_by_xpath(".//span[@class='ratingDate']").get_attribute("title")
    title = reviews[i].find_element_by_xpath(".//span[@class='noQuotes']").text
    review = reviews[i].find_element_by_xpath(".//p[@class='partial_entry']").text.replace("\n", "")
    # Save to CSV
    csvWriter.writerow((score, date, title, review))

# Close CSV file and browser
csvFile.close()
driver.close()