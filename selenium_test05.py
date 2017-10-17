
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("user-agent='Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'")

driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(10)
driver.get("https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html")

# page = driver.find_elements_by_xpath("//div[@class='page']")
# driver.execute_script("arguments[0].scrollIntoView()",page[1])
#
# continue_read = driver.find_element_by_xpath("//div[@class='flod-button' and @data-flod-fun='continue-read']")
# continue_read.click()
#
# page = driver.find_elements_by_xpath("//div[@class='page']")
# driver.execute_script("arguments[0].scrollIntoView();",page[-1])
#
# nextpage = driver.find_element_by_xpath("//a[@data-fun='next']")
# nextpage.click()

