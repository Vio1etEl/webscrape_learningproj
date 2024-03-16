# Name: El
# Time: 2024/3/14 15:27
import requests
from bs4 import BeautifulSoup
url = 'http://books.toscrape.com/'
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content,'html.parser')
all_price = soup.findAll('p',attrs={'class':'price_color'})
# print(all_price)  # 返回值为对象 <p class="price_color">Â£51.77</p>
for price in all_price:
    print(price.string)  # 将对象中的字符串输出  Â£51.77
all_title = soup.findAll('h3')
print(all_title)
for title in all_title:
#<h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>,
    all_link = title.findAll('a')
    for title_name in all_link:
        print(title_name.string)