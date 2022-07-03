
import time
from selenium.webdriver.chrome import webdriver
driver = webdriver.WebDriver()
driver.get("https://www.baidu.com")
time.sleep(5)
driver.quit()
stop_word_list