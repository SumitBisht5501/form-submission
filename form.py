from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configure the webdriver (use ChromeDriver)
driver = webdriver.Chrome()

# Open the Google Form
form_url = "https://forms.gle/WT68aV5UnPajeoSc8"
driver.get(form_url)

# Wait for the page to load
time.sleep(5)




# 1st Question (e.g., Text Field)
first_field = driver.find_element(By.XPATH, '//input[@type="text"]')
first_field.send_keys("Sumit Singh Bisht")

# 2nd Question (e.g., Radio Button)
second_question = driver.find_element(By.XPATH, '(//div[@role="radio"])[1]')
second_question.click()

# 3rd Question (e.g., Checkbox)
checkbox = driver.find_element(By.XPATH, '(//div[@role="checkbox"])[1]')
checkbox.click("")

# Submit the form
submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]')
submit_button.click()

# Wait for submission to complete
time.sleep(5)

# Close the browser
driver.quit()


