import selenium
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver import ActionChains

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service = webdriver.ChromeService()
driver = webdriver.Chrome(options= option, service= service)
slider_url = "https://practice-automation.com/slider/"
driver.get(slider_url)
#Find slider
slider = driver.find_element(by="id", value="slideMe")


action = ActionChains(driver)
# click on mittle of element(slider)
action.click(slider).perform()
# click on specifeid location
# action.drag_and_drop_by_offset(slider, 115, 296).perform()
for x in range(1,100,10):
    action.drag_and_drop_by_offset(slider, x+15, 296).perform()

print(slider.location)
print(driver.find_element(by="xpath",value="//span[@id ='value']").text)