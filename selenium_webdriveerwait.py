from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = webdriver.ChromeService()

delay_url = "https://practice-automation.com/javascript-delays/"
driver = webdriver.Chrome(options= options, service= service)
driver.maximize_window()
driver.get(url=delay_url)
start_btn = driver.find_element(by='xpath', value= "//button[contains(@id,'start')]")
start_btn.click()
wait = WebDriverWait(driver, 12)

is_element = wait.until(lambda driver :driver.find_element(By.ID,"delay").get_attribute("value")=="Liftoff!")

if (is_element== True):
    print("&&&&&&&&&&&&&&&test passed&&&&&&&&&&&&&&&&&&&&&&")
else:
    print("&&&&&&&&&&&&&&&test failed&&&&&&&&&&&&&&&&&&&&&&")

driver.quit