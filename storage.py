from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By


import pickle
import pandas as pd
import time 

DEBUG = True


def save_cookies(driver):
    accept_cookie = driver.find_element(by=By.XPATH,  value="//button[@class='styles_button__p3ZKg styles_secondary__aSwfV styles_submit_button__5JsBY']").click()
    print("Clicked")
    time.sleep(5)
    driver.implicitly_wait(5)
    pickle.dump(driver.get_cookies(), open("cookies", "wb"))
    


def sleep_driver(driver, sec):
    time.sleep(sec)
    driver.implicitly_wait(sec)


def save_all_data(data):
    data_frame = pd.DataFrame(data)
    data_frame.to_excel("data_fiels/data.xlsx")
    if DEBUG:
        print(data_frame)

# urls
url_instagram = "https://www.instagram.com"
url_stackowerflow = "https://stackoverflow.com"
url_my_user_agent = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
url_my_ip = "https://2ip.ru/"
url_webdriver_test = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
url_kufar_videocards = r"https://www.kufar.by/l/r~belarus?ar=&ot=1&query=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D1%8B&rgn=all"
url_tiktok = "https://www.tiktok.com"

# fake useragent
useragent = UserAgent() 

# options
options = webdriver.ChromeOptions()
options.add_argument(f"--user-agent={useragent.random}")
# options.add_argument(f"--headless")
options.add_argument("--start-maximized")
options.add_argument(f"--disable-blink-features=AutomationControlled")
# off errors in console
options.add_experimental_option('excludeSwitches', ['enable-logging'])


# driver
service = Service(r"C:\Users\Maks\Desktop\myfolder\Programming\Python\browser-automation-testing\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

