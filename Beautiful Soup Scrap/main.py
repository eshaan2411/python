from unicodedata import name
from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
response.raise_for_status()

webpage = response.text
soup = BeautifulSoup(markup=webpage, features="html.parser")

articles = [article.text for article in soup.find_all(name="a", class_="storylink")]
article_links = []
for article in soup.find_all(name="a", class_="storylink"):
    article_links.append(article.get("href"))

upvotes = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name="span", class_="score")]

max_upvotes = max(upvotes)
print(max_upvotes)
pos = upvotes.index(max_upvotes)
print("Found at pos: ", pos)

