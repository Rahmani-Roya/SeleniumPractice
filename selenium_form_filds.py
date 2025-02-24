from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver import chrome
# from selenium.webdriver.support.ui import  WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service = Service()
form_filds_url = "https://practice-automation.com/form-fields/"
driver = webdriver.Chrome(options= options, service= service)
driver.get(form_filds_url)
driver.maximize_window()
# Enter user name and password
name_input =driver.find_element(by="xpath", value="//input[@id = 'name-input']")
name_input.click()
name_input.send_keys("Roya Rahmani")
pass_input = driver.find_element(by="xpath", value="//input[@type = 'password']")
pass_input.click()
pass_input.send_keys("1234567")
# Find favorite drink
drink_checkbox = driver.find_element(by="id", value="drink2")
drink_checkbox.click()
drink_checkbox = driver.find_element(by="id", value="drink4")
drink_checkbox.click()
# Find color radio button
color_radiobutton = driver.find_element(by="id", value="color1")
# Scroll to color radiobutton
action = ActionChains(driver)
action.scroll_to_element(color_radiobutton).perform()
# Select radio button
color_radiobutton.click()

# Find drop down select
select_dropdown = driver.find_element(by="id", value="automation")
# Scroll to drop down select
action = ActionChains(driver)
action.scroll_to_element(select_dropdown).perform()
# Select drop down select
select_dropdown.click()
answer_dropdown = driver.find_element(by="xpath", value="//option[@data-testid='automation-yes']")
answer_dropdown.click()
# Find E mail
email_textbox = driver.find_element(by="id", value="email")
action = ActionChains(driver= driver)
action.scroll_to_element(email_textbox).perform()
email_textbox.click()
email_textbox.send_keys("rahmani.roya.pro@gmail.com")

# Find Message
message_textbox = driver.find_element(by="id", value="message")
action = ActionChains(driver= driver)
action.scroll_to_element(message_textbox).perform()
message_textbox.click()
message_textbox.send_keys("it is a Test")

# Find Submit button
submit_btn = driver.find_element(by="xpath", value="//button[@id = 'submit-btn']")
# Scroll to Submit button
action = ActionChains(driver)
action.scroll_to_element(submit_btn).perform()
submit_btn.click()
