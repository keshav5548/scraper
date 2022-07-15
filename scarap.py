import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.truecaller.com/search/in/7888965734').text # Getting page HTML through requestsoup = BeautifulSoup(page, 'lxml') # Parsing content using beautifulsoup
soup=BeautifulSoup(page,'lxml'); # Display the innerText of e
# print(soup.prettify())
names=soup.find_all('div')
for n in names :
 print(n.text)