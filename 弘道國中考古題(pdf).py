import os
import requests
from bs4 import BeautifulSoup

folderPath = "弘道國中題庫(pdf)"
if not os.path.exists(folderPath):
    os.mkdir(folderPath)

url = "https://www.htjh.tp.edu.tw/office/div_200/section_210/s2101_desc/%e8%87%aa%e7%84%b6/"
headers = {"User-Agent":"Mozilla/5.0"}
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")

downloaded = set()
for a in soup.select(".nojs_modal_list a[href$='.pdf']"):
    url = a["href"]
    filename = a.text.strip()
    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"
    for c in '/\\?*:|"<>':
        filename = filename.replace(c, "_")

    if filename in downloaded:
        continue
    downloaded.add(filename)

    r = requests.get(url)
    with open(os.path.join(folderPath, filename), "wb") as f:
        f.write(r.content)
    print(f"下載成功：{filename}")

#社會科題目下載

base_url = "https://www.htjh.tp.edu.tw/office/div_200/section_210/s2101_desc/%e7%a4%be%e6%9c%83/#tab2"
headers = {"User-Agent":"Mozilla/5.0"}
resp = requests.get(base_url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")

for a in soup.select(".nojs_modal_list a[href$='.pdf']"):
    url = a["href"]
    filename = a.text.strip()
    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"
    # 過濾檔名中的非法字元
    for c in '/\\?*:|"<>':
        filename = filename.replace(c, "_")
    # 下載
    r = requests.get(url)
    with open(os.path.join("弘道國中題庫(pdf)", filename), "wb") as f:
        f.write(r.content)
    print(f"下載成功：{filename}")

#數學科下載

base_url = "https://www.htjh.tp.edu.tw/office/div_200/section_210/s2101_desc/%e6%95%b8%e5%ad%b8/"
headers = {"User-Agent":"Mozilla/5.0"}
resp = requests.get(base_url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")

for a in soup.select(".nojs_modal_list a[href$='.pdf']"):
    url = a["href"]
    filename = a.text.strip()
    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"
    # 過濾檔名中的非法字元
    for c in '/\\?*:|"<>':
        filename = filename.replace(c, "_")
    # 下載
    r = requests.get(url)
    with open(os.path.join("弘道國中題庫(pdf)", filename), "wb") as f:
        f.write(r.content)
    print(f"下載成功：{filename}")



#英文科下載


base_url = "https://www.htjh.tp.edu.tw/office/div_200/section_210/s2101_desc/%e8%8b%b1%e8%aa%9e%e6%96%87/"
headers = {"User-Agent":"Mozilla/5.0"}
resp = requests.get(base_url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")

for a in soup.select(".nojs_modal_list a[href$='.pdf']"):
    url = a["href"]
    filename = a.text.strip()
    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"
    # 過濾檔名中的非法字元
    for c in '/\\?*:|"<>':
        filename = filename.replace(c, "_")
    # 下載
    r = requests.get(url)
    with open(os.path.join("弘道國中題庫(pdf)", filename), "wb") as f:
        f.write(r.content)
    print(f"下載成功：{filename}")

#國文科下載


base_url = "https://www.htjh.tp.edu.tw/office/div_200/section_210/s2101_desc/%e5%9c%8b%e8%aa%9e%e6%96%87/"
headers = {"User-Agent":"Mozilla/5.0"}
resp = requests.get(base_url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")

for a in soup.select(".nojs_modal_list a[href$='.pdf']"):
    url = a["href"]
    filename = a.text.strip()
    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"
    # 過濾檔名中的非法字元
    for c in '/\\?*:|"<>':
        filename = filename.replace(c, "_")
    # 下載
    r = requests.get(url)
    with open(os.path.join("弘道國中題庫(pdf)", filename), "wb") as f:
        f.write(r.content)
    print(f"下載成功：{filename}")




    
