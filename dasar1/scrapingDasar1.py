from selenium import webdriver  # Import library Selenium untuk automasi browser
from selenium.webdriver.chrome.service import Service  # Import Service untuk menentukan lokasi chromedriver
from bs4 import BeautifulSoup  # Import BeautifulSoup untuk parsing HTML
import pandas as pd  # Import pandas untuk manipulasi data dan ekspor ke Excel
import time  # Import time untuk memberikan jeda (sleep)

option = webdriver.ChromeOptions()  # Membuat opsi untuk Chrome
option.add_argument('--headless')  # Menjalankan Chrome tanpa tampilan GUI (headless)
servis = Service('chromedriver.exe')  # Menentukan lokasi file chromedriver
driver = webdriver.Chrome(service=servis, options=option)  # Membuat objek driver Chrome dengan opsi dan service

url_web = "https://sandbox.oxylabs.io/products/category/pc"  # URL website yang akan di-scrape
driver.set_window_size(1920, 1080)  # Mengatur ukuran jendela browser
driver.get(url_web)  # Membuka halaman web
time.sleep(5)  # Menunggu 5 detik agar halaman termuat sempurna

driver.save_screenshot("gambar.png")  # Menyimpan screenshot halaman web
content = driver.page_source  # Mengambil source HTML dari halaman web
driver.quit()  # Menutup browser

soup = BeautifulSoup(content, 'html.parser')  # Membuat objek BeautifulSoup untuk parsing HTML

listNama, listTags, listHarga, listStok = [], [], [], []  # Membuat list kosong untuk menampung data hasil scraping

a = 1  # Variabel untuk menghitung proses data
for area in soup.find_all('div', class_="product-card css-e8at8d eag3qlw10"):  # Loop setiap produk pada halaman
    print('proses data ke-' +str(a))  # Menampilkan proses data ke berapa

    nama = area.find('h4', class_="title css-7u5e79 eag3qlw7").get_text()  # Mengambil nama produk

    tags = area.find('p', class_="category css-8fdgzc eag3qlw9")  # Mengambil elemen tags/kategori
    if tags:
        tags = " | ".join([tag.get_text() for tag in tags])  # Jika ada, gabungkan semua tag menjadi satu string

    harga = area.find('div', class_="price-wrapper css-li4v8k eag3qlw4").get_text()  # Mengambil harga produk

    stok = area.find('p', class_="in-stock css-1w904rj eag3qlw1")  # Cek apakah produk tersedia (in stock)
    if not stok:
        stok = area.find('p', class_="out-of-stock css-uo03ln eag3qlw0")  # Jika tidak, cek out of stock
    stok = stok.get_text()  # Mengambil teks status stok

    listNama.append(nama)  # Menambahkan nama ke list
    listTags.append(tags)  # Menambahkan tags ke list
    listHarga.append(harga)  # Menambahkan harga ke list
    listStok.append(stok)  # Menambahkan stok ke list

    a += 1  # Menambah counter proses data
    print("--------------------")  # Menampilkan pemisah antar data

df = pd.DataFrame({'nama': listNama, 'tags': listTags, 'harga': listHarga, 'stok': listStok})  # Membuat DataFrame dari list hasil scraping
with pd.ExcelWriter('dataGamePc.xlsx') as writer:  # Membuka writer untuk file Excel
    df.to_excel(writer, sheet_name='sheet1', index=False)  # Menulis DataFrame ke file Excel tanpa index

















# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# option = webdriver.ChromeOptions()
# option.add_argument('--headless')
# servis = Service('chromedriver.exe')
# driver = webdriver.Chrome(service=servis, options=option)  # Fixed line

# url_web = "https://sandbox.oxylabs.io/products/category/pc"
# driver.set_window_size(1920, 1080)
# driver.get(url_web)
# time.sleep(5)

# driver.save_screenshot("gambar.png")
# content = driver.page_source
# driver.quit()

# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.encode('utf-8'))

# listNama, listTags, listHarga, listStok = [], [], [], []

# a = 1
# for area in soup.find_all('div', class_="product-card css-e8at8d eag3qlw10"):
#     print('proses data ke-' +str(a))
#     nama = area.find('h4', class_="title css-7u5e79 eag3qlw7").get_text()
#     tags = area.find('p', class_="category css-8fdgzc eag3qlw9")
#     if tags:
#         tags = " | ".join([tag.get_text() for tag in tags])

#     harga = area.find('div', class_="price-wrapper css-li4v8k eag3qlw4").get_text()
#     stok = area.find('p', class_="in-stock css-1w904rj eag3qlw1")
#     if not stok:
#         stok = area.find('p', class_="out-of-stock css-uo03ln eag3qlw0")
#     stok = stok.get_text()

#     listNama.append(nama)
#     listTags.append(tags)
#     listHarga.append(harga)
#     listStok.append(stok)
#     # print(
#     #     f"nama game: {nama} \n"
#     #     f"tags: {tags}\n"
#     #     f"harga: {harga}\n"
#     #     f"stok: {stok}"
#     # )
#     a += 1
#     print("--------------------")

# df = pd.DataFrame({'nama': listNama, 'tags': listTags, 'harga': listHarga, 'stok': listStok})
# with pd.ExcelWriter('dataGamePc.xlsx') as writer:
#     df.to_excel(writer, sheet_name='sheet1', index=False)