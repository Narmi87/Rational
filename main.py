from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.royalroad.com/fiction/47997/overkill'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="row fic-header")
details = soup.find_all('div', class_="fiction-info")

with open('webserial.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Author', 'Status', 'Tags']
    thewriter.writerow(header)

    for list_ in lists:
        title = list_.find('h1', property="name").text.replace('\n', '')
        author = list_.find('span', property="name").text.replace('\n', '')
        print(title, author)
    for detail in details:
        status = detail.find_all('span', class_="label label-default label-sm bg-blue-hoki")
        print(status)
        for stat in status:
            print(stat.text)
        tags = detail.find_all('a', property="genre")
        print(tags)
        for tag in tags:
            print(tag.text)

        info = [title, author, status, tags]
        thewriter.writerow(info)
