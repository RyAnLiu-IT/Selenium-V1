from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')


driver = webdriver.Chrome('/home/ec2-user/environment/chromedriver', chrome_options=options)


driver.get("https://medicpare.site/searchDoctor_1.html")


Q1 = driver.find_element_by_id('search')
Q1.clear()
Q1.send_keys("Wong")

time.sleep(15)

driver.save_screenshot('screenshot.png')

driver.close()