import selenium
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome import service
option = webdriver.ChromeOptions()
servic = webdriver.ChromeService()
option.add_experimental_option("detach", True)
modal_url = "https://practice-automation.com/modals/"
driver = webdriver.Chrome(options= option, service= servic)
driver.get(modal_url)
driver.find_element(by="xpath", value="//button[@id='simpleModal']").click()
driver.find_element(by="xpath", value="//div[@class='pum-content popmake-content']").click()