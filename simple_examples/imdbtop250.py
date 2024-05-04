import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
html_icerik = response.content
soup = BeautifulSoup(html_icerik,"html.parser")






basliklar = soup.find_all("div",{"class":"sc-b0691f29-0 jbYPfh cli-children"})
ratingler = soup.find_all("div",{"class","sc-e2dbc1a3-0 ajrIH sc-b0691f29-2 bhhtyj cli-ratings-container"})

for baslik,rayting in zip(basliklar,ratingler):

    baslik = baslik.text
    rayting = rayting.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")


    print(f"Film adı: {baslik} Film rayting: {rayting}")
