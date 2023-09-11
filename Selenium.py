from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.implicitly_wait(10)
driver.find_element_by_name("q").send_keys("webdriver")
driver.find_element_by_name("btnK").click()
driver.quit()

driver = webdriver.Chrome()
driver.get("testerlaru.temp.swtest.ru/index.php?route=account/login")
driver.implicitly_wait(10)

driver.find_element_by_name("password").send_keys("QA_12345678")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/form/input").click()
