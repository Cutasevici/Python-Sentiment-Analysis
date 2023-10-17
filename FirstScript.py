import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to scroll and load comments, then extract them
def scrape_youtube_comments(video_url, comment_limit):
    driver = webdriver.Chrome()
    driver.get(video_url)

    # Wait for the comments section to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#comments")))

    # Scroll to load comments
    while True:
        try:
            # Scroll down to load more comments
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)  # Wait for the comments to load

            # Check if comment limit is reached
            if len(driver.find_elements(By.CSS_SELECTOR, "#content-text")) >= comment_limit:
                break
        except:
            break

    # Extract comments
    comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")
    comment_texts = [comment.text for comment in comments[:comment_limit]]

    # Close the WebDriver
    driver.quit()

    return comment_texts

# Example YouTube video URL
video_url = 'https://www.youtube.com/watch?v=VvQiMC0mvGg'

# Limit the number of comments to scrape
comment_limit = 99

# Scrape comments
comments = scrape_youtube_comments(video_url, comment_limit)

# Create a dictionary to store comments
data = {"comments": comments}

# Save data to JSON file
output_file = 'RawComments.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"{len(comments)} comments successfully saved to {output_file}")
