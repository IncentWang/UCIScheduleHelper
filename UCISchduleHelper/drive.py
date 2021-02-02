from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

OutputPath = 'REPLACE_WITH_PATH'

f = open(OutputPath, 'w')

driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
# REPLACE_WITH_PATH

driver.get('https://www.reg.uci.edu/perl/WebSoc')

for i in range(1, 148):
    selectTag = Select(driver.find_element_by_name('Dept'))
    selectTag.select_by_index(i)
    driver.find_element_by_xpath("/html/body/font/form/p[2]/input[2]").click()
    f.write(driver.page_source)
    driver.back()
    time.sleep(0.1)

f.close()

time.sleep(20)