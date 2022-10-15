
import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html,'lxml')
    return soup

def get_data(soup):
    catalog = soup.find('div',class_ = 'Tag--articles')
    news = catalog.find_all('div',class_ = 'Tag--article')


    for new in news:
        title = new.find('a',class_= 'ArticleItem--name').text.strip()
        image = new.find('img',class_ = 'ArticleItem--image-img').get('data-src')
        

        write_csv({
            'title':title,
            'image':image,
        })

def write_csv(data):
    with open('news.csv','a') as file:
        names = ['title','image']
        write = csv.DictWriter(file, delimiter=',',fieldnames=names)
        write.writerow(data)


def main():
    try:
        for i in range(1,10):
            BASE_URL = f'https://kaktus.media/?lable=8&date=2022-10-15&order=time{i}'
            html = get_html(BASE_URL)
            soup = get_soup(html)
            get_data(soup)
            print(f'спарсили {i} страницу')
    except AttributeError:
        print('это последняя страница')

if __name__ == '__main__':
    main()
