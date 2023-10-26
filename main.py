from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on
cookies = driver.find_element(By.CSS_SELECTOR, "div #cookie")

five_min = time.time() + 60*5
time_out = time.time() +5

right_pannel = driver.find_elements(By.CSS_SELECTOR,"div b")

right_pannel_list = [item.text.split("-") for item in right_pannel][10:]

updated_right_pannel_list = right_pannel_list[:8]

updated_right_pannel_list.reverse()





while five_min>time.time():
    cookies.click()
    if time.time()>time_out:
        total_cookies = driver.find_element(By.CSS_SELECTOR, "div #money")

        for i in updated_right_pannel_list:
            booster = i[0].strip()

            find = driver.find_element(By.XPATH,f'//*[@id="buy{booster}"]')

            try:
                find.click()
            except:
                pass

        time_out += 5  # 5 sec break


#after 5 min
cookies_second = driver.find_element(By.CSS_SELECTOR,"div #cps")
print(cookies_second.text)
driver.close()


