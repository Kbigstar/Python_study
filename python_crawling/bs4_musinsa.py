from bs4 import BeautifulSoup
import requests

def get_musinsa(page):
    url = f'https://www.musinsa.com/mz/community-info?p={page}'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    arr = []
    print(soup.prettify())

    table = soup.select_one('.ul-col')
    lis = table.find_all('li')
    for li in lis:
        if 'col-list' in li['class']:
            print(li.select_one('.colName'))
            spans = li.find_all('span')
            div = li.find_all('div')
            print(div)
            cate = spans[0].text
            a_tags = spans[2].find_all('a')
            href = a_tags[1].get('href')
            # print(a_tags.text)
            title = a_tags[1].text
            date = spans[4].text
            cool = spans[5].text
            hmm = spans[6].text
            hit = spans[7].text
            arr.append([cate,href,title,date,cool,hmm,hit])

    import csv
    with open('musinsa.csv', 'a', encoding='utf-8', newline='') as f:
        write = csv.writer(f, delimiter='|')
        write.writerows(arr)

if __name__ == '__main__':
    for i in range(1, 11):
        get_musinsa(i)