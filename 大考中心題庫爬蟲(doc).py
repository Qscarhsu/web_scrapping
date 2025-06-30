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

folderPath = "大考中心題庫(doc)"

if not os.path.exists(folderPath):
    os.mkdir(folderPath)


list = []

for i in range(1,11):
    url = f"https://www.ceec.edu.tw/xmfile?xsmsid=0J052424829869345634&page={i}"
    
    driver.get(url)

    # dict = {f"第{i}頁":[]}

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.file_ext.file_doc")))

        datas = driver.find_elements(By.CSS_SELECTOR, "a.file_ext.file_doc")

        titles = driver.find_elements(By.CSS_SELECTOR, "td.title")

        for url in datas:
            # print(url.get_attribute("href"))

            list.append(url.get_attribute("href"))


    
    except TimeoutError:
            print("等待逾時")
            pass
    
with open("大考中心考古題.json", "w", encoding= "utf-8") as file:
     
     file.write(json.dumps(list, ensure_ascii= False, indent=4))
    
for url_ in list:
     
    n = list.index(url_)

    os.system(f"curl {url_} -o 大考中心題庫(doc)/test{n}.doc")