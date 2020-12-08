import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("http://customform.jp/form/input/46755/")
time.sleep(10)
driver.find_element_by_xpath(
    "//input[@name='question_434724']").send_keys("G2004155")
driver.find_element_by_xpath(
    "//input[@name='question_434727']").send_keys("WU ZHEN")
Select(driver.find_element_by_name(
    "question_434726")).select_by_value("院進学C3")
driver.find_element_by_xpath("//input[@name='question_434728']").click()
date=str(str(datetime.datetime.now().year)+"/"
         +str(datetime.datetime.now().month)+"/"
         +str(datetime.datetime.now().day))
driver.find_element_by_xpath(
    "//input[@name='question_435964']").send_keys(date)
driver.find_element_by_id("customform-submit").click()
driver.quit()
