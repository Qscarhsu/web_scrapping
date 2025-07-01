import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# 你的目標網址
base_url = "https://www.lintingmath.url.tw/subject/"
target_url = "https://www.lintingmath.url.tw/hot_59659.html"

headers = {"User-Agent": "Mozilla/5.0"}

# 建立儲存資料夾
folder = "林庭數學(pdf)"
os.makedirs(folder, exist_ok=True)

resp = requests.get(target_url, headers=headers)
resp.encoding = 'utf-8' 
soup = BeautifulSoup(resp.text, "html.parser")

# 選取所有 PDF 超連結
for a in soup.select('a[href$=".pdf"]'):
    href = a["href"]
    print(a.text)
    # 修正相對網址（支援 //xxx.pdf 與 /xxx.pdf）
    if href.startswith("//"):
        pdf_url = "https:" + href
    else:
        pdf_url = urljoin(base_url, href)

    # 取連結顯示的中文名稱做檔名
    filename = a.text.strip()
    if not filename.lower().endswith('.pdf'):
        filename += ".pdf"
    # 過濾非法字元
    for c in '/\\?*:|"<>':
        filename = filename.replace(c, "_")
    save_path = os.path.join(folder, filename)

    # 開始下載
    print(f"下載：{pdf_url} → {filename}")
    r = requests.get(pdf_url)
    with open(save_path, "wb") as f:
        f.write(r.content)

print("全部下載完成！")


#高一 高二名校考古題解答 (高三網站連結失效)

scrapping_list = [
    "https://www.lintingmath.url.tw/hot_cg1219.html",
    "https://www.lintingmath.url.tw/hot_cg1221.html"
]

for scrapping_web in scrapping_list:
    resp = requests.get(scrapping_web, headers=headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, "html.parser")

    for a in soup.select('a.titleC'):
        detail_url = urljoin(scrapping_web, a['href'])
        resp = requests.get(detail_url, headers=headers)
        resp.encoding = 'utf-8'
        soup2 = BeautifulSoup(resp.text, "html.parser")

        for b in soup2.select('ul li a[href$=".pdf"]'):
            pdf_url = urljoin(detail_url, b["href"])
            # 過濾非法字元
            filename = b.text.strip()
            filename = re.sub(r'[\\/:"*?<>|]+', "_", filename)
            if not filename.lower().endswith('.pdf'):
                filename += ".pdf"
            save_path = os.path.join(folder, filename)
            print(f"下載: {pdf_url} → {save_path}")

            # 下載 PDF (用 requests 取代 os.system 更穩定)
            try:
                r = requests.get(pdf_url)
                with open(save_path, "wb") as f:
                    f.write(r.content)
            except Exception as e:
                print(f"下載失敗：{pdf_url}，原因：{e}")

print("全部下載完成")













