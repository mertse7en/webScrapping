from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


PATH = "C:\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net/")

search = driver.find_element_by_name("s")
search.clear()
search.send_keys("python")
search.send_keys(Keys.RETURN)


try : 
    element =  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Next →")))
    element.click()
except :
    print("elementi bulamiyorum!!!!!!!")


