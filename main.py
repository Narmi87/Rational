from bs4 import BeautifulSoup
import requests
import csv

RR_list = open("stories_links").read().splitlines()
print(len(RR_list))

RR_list = list(dict.fromkeys(RR_list))
print(len(RR_list))


with open('serial.csv', 'w', encoding='utf8', newline='\n') as f:
    writer = csv.writer(f)
    header = ['Title', 'Author', 'Type', 'Status', 'Tags']
    writer.writerow(header)


def get_info(url):
    for x in url:
        print(x)
        page = requests.get(x)

        soup = BeautifulSoup(page.content, 'html.parser')
        lists = soup.find_all('div', class_="row fic-header")
        status = soup.find_all('div', class_="fiction-info")
        tags = soup.find_all('span', class_="tags")

        # print(status)
        # print(tags.text)

        with open('serial.csv', 'a', encoding='utf8', newline='\n') as file:
            writer2 = csv.writer(file)

            for list_ in lists:
                title = list_.find('h1', property="name").text
                author = list_.find('span', property="name").text.replace('\n', '')
                print(title, author)
            for stat in status:
                type_ = stat.find_all('span', class_="bg-blue-hoki")[0].text
                current_status = stat.find_all('span', class_="bg-blue-hoki")[1].text.strip()
                print(type_, current_status)
            for tag in tags:
                item = ", ".join([tag.text for tag in tag.find_all("a")])
                print(item)

            writer2.writerow([title, author, type_, current_status, item])


get_info(RR_list)
