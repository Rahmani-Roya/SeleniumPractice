import selenium
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome import service
def select_date(year, month, day):
    calender_url = "https://practice-automation.com/calendars/"
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    servise = webdriver.ChromeService()
    driver = webdriver.Chrome(options=option,service=servise)
    driver.get(calender_url)
    driver.maximize_window()
    driver.find_element(by= "xpath", value="//input[@id='g1065-2-1-selectorenteradate']").click()
    while(True):
        current_year = driver.find_element(by= "xpath", value="//span[@class='ui-datepicker-year']")
        if (current_year.text== year):
            break;
        elif(current_year.text < year):
            driver.find_element(by="xpath", value="//a[@data-handler='next']").click()
        elif (current_year.text > year):
            driver.find_element(by="xpath", value="//a[@data-handler='prev']").click()
    while(True):
        current_month = driver.find_element(by= "xpath", value="//span[@class='ui-datepicker-month']")
        if (current_month.text== month):
            break;
        elif(current_month.text < month):
            driver.find_element(by="xpath", value="//a[@data-handler='next']").click()
        elif(current_month.text > month):
            driver.find_element(by="xpath", value="//a[@data-handler='prev']").click()

    driver.find_element(by="xpath", value=f"//table//a[@data-date= {day}]").click()

select_date("2023","August", "13")
