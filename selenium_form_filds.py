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
# Find Submit button
submit_btn = driver.find_element(by="xpath", value="//button[@id = 'submit-btn']")
# Scroll to Submit button
action = ActionChains(driver)
action.scroll_to_element(submit_btn).perform()
submit_btn.click()