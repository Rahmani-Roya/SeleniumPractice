import selenium
from selenium import webdriver
from selenium.webdriver.common import service

popup_url = "https://practice-automation.com/popups/"
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service = webdriver.ChromeService()
driver = webdriver.Chrome(options=option, service= service)

driver.get(popup_url)
driver.find_element(by="id", value="alert").click()
driver.switch_to.alert.dismiss()
driver.find_element(by="id", value="confirm").click()
driver.switch_to.alert.dismiss()
if (driver.find_element(by="id", value="confirmResult").text == "Cancel it is!"):
    print("you have canceled!!!!!")
driver.find_element(by="id", value="confirm").click()
driver.switch_to.alert.accept()
if (driver.find_element(by="id", value="confirmResult").text == "OK it is!"):
    print("it is OK!!!")
driver.find_element(by="id", value="prompt").click()
message = "Roya!"
driver.switch_to.alert.send_keys(message)
driver.switch_to.alert.accept()
if (driver.find_element(by="id", value="promptResult").text == f"Nice to meet you, {message}!"):
     print("you klicked OK in prompt popup!!!")
else:
     print("you klicked cancel in prompt popup!!!")
driver.find_element(by="xpath", value="//div[@class ='tooltip_1']").click()
if (driver.find_element(by="id", value="myTooltip").text=="Cool text"):
     print("You clicked tooltip")





