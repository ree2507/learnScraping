import requests
import pandas as pd
from bs4 import BeautifulSoup

# response = requests.get("https://sandbox.oxylabs.io/products/category/pc/page_num=1")


baseUrl = "https://sandbox.oxylabs.io/products/category/pc"
page_num = 1
result = []
for page_num in range(1,4):
    url = f"{baseUrl}?page_num={page_num}"
    print(f"Scraping page: {url}")

    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the page or no more pages available.")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    produk = soup.find_all("div", class_="product-card css-e8at8d eag3qlw10")

    if not produk:
        print("No more data found, ending the scraping process.")
        break

    for item in produk:
        nameGames = item.find("h4", class_="title css-7u5e79 eag3qlw7").get_text(strip=True)

        tags = item.find('p', class_="category css-8fdgzc eag3qlw9")  # Mengambil elemen tags/kategori
        if tags:
            tags = " | ".join([tag.get_text() for tag in tags])  # Jika ada, gabungkan semua tag menjadi satu string

        price = item.find("div", class_="price-wrapper css-li4v8k eag3qlw4").get_text(strip=True)
        
        # stok = item.find('p', class_="in-stock css-1w904rj eag3qlw1")
        # if not stok:
        #     stok = item.find('p', class_="out-of-stock css-uo03ln eag3qlw0")
        # stok = stok.get_text(strip=True) if stok else "Unknown"

        result.append((nameGames, tags, price))

df = pd.DataFrame(result, columns=['Name', 'Tags', 'Price'])
with pd.ExcelWriter('dataGamePc.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1', index=False)

















    # data = soup.find("div", class_="products-wrapper css-phdzty e1kord975")
# result = []

# for i in data.find_all("div", class_="product-card css-e8at8d eag3qlw10"):
#     nameGames = i.find("h4", class_="title css-7u5e79 eag3qlw7").get_text(strip=True)

#     tags = i.find('p', class_="category css-8fdgzc eag3qlw9")  # Mengambil elemen tags/kategori
#     if tags:
#         tags = " | ".join([tag.get_text() for tag in tags])  # Jika ada, gabungkan semua tag menjadi satu string

#     price = i.find("div", class_="price-wrapper css-li4v8k eag3qlw4").get_text(strip=True)
    
#     # stok = i.find('p', class_="in-stock css-1w904rj eag3qlw1")
#     # if not stok:
#     #     stok = i.find('p', class_="out-of-stock css-uo03ln eag3qlw0")
#     # stok = stok.get_text(strip=True) if stok else "Unknown"

#     result.append((nameGames, tags, price))