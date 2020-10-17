"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\webdrivers\chromedriver.exe"
#close_tab = "/html/body/div[11]/div/div/a"

driver = webdriver.Chrome(PATH)
driver.get("https://www.hepsiburada.com/ara?q=ps4")

driver.implicitly_wait(5)

click_button = driver.find_element_by_class_name("hb-pl-cn")

click_button.click()
actions.perform()


"""

f = open("ilk-deneme.xlsx", "r")
print(f.read())
