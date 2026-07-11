import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books=[]

for item in soup.find_all("article", class_="product_pod"):

    title = item.h3.a["title"]

    price = item.find("p", class_="price_color").text

    price = price.replace("Â","")

    books.append([title, price])

df = pd.DataFrame(books, columns=["Book Name","Price"])

print(df)

df.to_csv("books_dataset.csv", index=False, encoding="utf-8")

print("Dataset saved successfully")