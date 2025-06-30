from selenium.webdriver.chrome.service import Service
from selenium import webdriver


from selenium.common.exceptions import TimeoutException

# 面對動態網頁，等待某個元素出現的工具，通常與 exptected_conditions 搭配
from selenium.webdriver.support.ui import WebDriverWait

# 搭配 WebDriverWait 使用，對元素狀態的一種期待條件，若條件發生，則等待結束，往下一行執行
from selenium.webdriver.support import expected_conditions as EC

# 期待元素出現要透過什麼方式指定，通常與 EC、WebDriverWait 一起使用
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

# 強制等待 (執行期間休息一下)
from time import sleep

import os

import json

my_options = webdriver.ChromeOptions()
my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
# my_options.add_argument("--start-maximized")         #最大化視窗
# my_options.add_argument("--incognito")               #開啟無痕模式
# my_options.add_argument("--disable-popup-blocking") #禁用彈出攔截
# my_options.add_argument("--disable-notifications")  #取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  #設定為正體中文


driver = webdriver.Chrome(
    options = my_options,
)

folderPath = "龍華國中題庫(pdf)"

if not os.path.exists(folderPath):
    os.mkdir(folderPath)


list = []

for i in range(2,5):
    url = f"https://affairs.kh.edu.tw/upload/upload_list/3850/16/{i}"
    
    driver.get(url)

    # dict = {f"第{i}頁":[]}

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.upload_list_table a")))

        datas = driver.find_elements(By.CSS_SELECTOR, "table.upload_list_table a")


        for url in datas:
            # print(url.get_attribute("href"))

            list.append(url.get_attribute("href"))

    except TimeoutError:
        print("error")
        pass

test_list = []

for url_ in set(list):
    driver.get(url_)
    try:
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#file_list a[href$=".pdf"]:not([href^="https://docs.google.com/"]')))

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "file_list")))

            datas = driver.find_elements(By.CSS_SELECTOR, '#file_list a[href$=".pdf"]:not([href^="https://docs.google.com/"]')

            



            for url_01 in datas:
                # print(url.get_attribute("href"))

                test_list.append(url_01.get_attribute("href"))

                os.system(f"curl {url_01.get_attribute("href")} -o 龍華國中題庫(pdf)/{url_01.text}")

                print(f"{url_01.text}: 下載成功")

    except TimeoutError:
        print("error")
        pass