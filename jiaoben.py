import time
import datetime
import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("http://customform.jp/form/input/46755/")
time.sleep(0.3)
driver.find_element_by_xpath(
    "//input[@name='question_434724']").send_keys("G2004154")
driver.find_element_by_xpath(
    "//input[@name='question_434727']").send_keys("YANG YIZHAN")
Select(driver.find_element_by_name(
    "question_434726")).select_by_value("中級C4")
driver.find_element_by_xpath("//input[@name='question_434728']")
date=str(str(datetime.datetime.now().year)+"/"
         +str(datetime.datetime.now().month)+"/"
         +str(datetime.datetime.now().day))
driver.find_element_by_xpath(
    "//input[@name='question_435964']").send_keys(date)
driver.find_element_by_id("customform-submit")
time.sleep(5)
driver.quit()
