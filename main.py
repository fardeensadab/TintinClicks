from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://10.220.20.12/index.php/home/login")
driver.maximize_window()

time.sleep(1)

user = ["fardeensadab", "sadmanahmed", "shahirawlad", "sameenyeaser"]
password = ["248", "Sadmed347", "0a4RMF1660", "12345"]
minutes = []


def find_smallest_number_index(numbers):
    smallest_index = 0  

    for index in range(1, len(numbers)):
        if numbers[index] < numbers[smallest_index]:
            smallest_index = index 

    return smallest_index

user_len = len(user)

for i in range(user_len):
    user_field = driver.find_element(By.ID, 'username')
    user_field.send_keys(user[i])

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password[i])
    password_field.send_keys(Keys.RETURN)

    tbody  = driver.find_elements(By.XPATH, '//*[@id="updates"]/div[1]/table/tbody/tr[6]/td[2]')
    tx = tbody[0]
    ty = tx.text
    minutes.append(int(ty.split()[0]))
    # print(tx.text)
    # print(minutes_value)

    time.sleep(3)

    logout = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/ul/li[4]/a')
    logout[0].click()

smallest_index = find_smallest_number_index(minutes)
print(minutes)
print(smallest_index)

driver.get("http://router.miwifi.com/cgi-bin/luci/web")
router_password_field = driver.find_element(By.ID, 'password')
router_password_field.send_keys('11151115')
router_password_field.send_keys(Keys.RETURN)
time.sleep(3)

settings = driver.find_element(By.XPATH, '//*[@id="nav"]/ul/li[2]/a')
settings.click()
net_settings = driver.find_element(By.XPATH, '//*[@id="hd"]/div/div[2]/ul/li[2]/a/span')
net_settings.click()
time.sleep(3)


# router_net_user_field = driver.find_elements(By.NAME, 'pppoeName')
# # router_net_user_field.clear()
# # router_net_user_field.send_keys(user[smallest_index])
# router_net_password_field = driver.find_elements(By.NAME, 'pppoePwd')
# # router_net_password_field.clear()
# # router_net_password_field.send_keys(user[smallest_index])
# # router_net_password_field.send_keys(Keys.RETURN)

router_net_user_field = driver.find_element(By.XPATH, '//*[@id="pppoe"]/div[1]/span/input')
router_net_user_field.clear()
router_net_user_field.send_keys(user[smallest_index])
router_net_password_field = driver.find_element(By.XPATH, '//*[@id="pppoe"]/div[2]/span/input')
router_net_password_field.clear()
router_net_password_field.send_keys(password[smallest_index])
router_net_password_field.send_keys(Keys.RETURN)

time.sleep(3)

dropdown_access = driver.find_element(By.XPATH, '//*[@id="sysmenu"]')
dropdown_access.click()
signout = driver.find_element(By.XPATH, '//*[@id="dropmenu"]/ul/li[5]/a')
signout.click()

time.sleep(3)

driver.close()