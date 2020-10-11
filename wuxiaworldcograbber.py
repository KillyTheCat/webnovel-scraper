from bs4 import BeautifulSoup as bs
import requests
import html5lib


def get_novel_text(novelname, chapternumber):
    url = 'https://www.wuxiaworld.co/' + novelname +'/'
    doc = requests.get(url)

    soup = bs(doc.content, 'html5lib')
    table = soup.find('div', attrs={'class':'chapter-wrapper'})

    chapterurls = []
    for row in table.find_all('a' , attrs={'class':'chapter-item'}):
        chapterurls.append(row['href'])

    url = 'https://www.wuxiaworld.co/' + chapterurls[chapternumber-1][1::]
    doc = requests.get(url)
    soup = bs(doc.content, 'html5lib')
    table = soup.find('div', attrs={'class': 'chapter-entity'})
    return(table.text)

def get_novel_text_by_url(novelurl, chapternumber):
    url = 'https://www.wuxiaworld.co' + novelurl
    doc = requests.get(url)

    soup = bs(doc.content, 'html5lib')
    table = soup.find('div', attrs={'class':'chapter-wrapper'})

    chapterurls = []
    for row in table.find_all('a' , attrs={'class':'chapter-item'}):
        chapterurls.append(row['href'])

    url = 'https://www.wuxiaworld.co/' + chapterurls[chapternumber-1][1::]
    doc = requests.get(url)
    soup = bs(doc.content, 'html5lib')
    table = soup.find('div', attrs={'class': 'chapter-entity'})
    return(table.get_text())

def find_novel(novelname):
    url = 'https://www.wuxiaworld.co/search/' + novelname.replace(' ','%20') + '/1'
    doc = requests.get(url)
    soup = bs(doc.content, 'html5lib')

    resultslist = soup.find('ul', attrs={'class':'result-list'})
    searchResults = []
    if(resultslist == None):
        return (404)   #not found code

    for items in resultslist.findAll('li', attrs={'class':'list-item'}):
        result = {}
        for i in items.findAll('div', attrs={'class':'item-info'}):
            result['name'] = i.a.text
            result['urlextension'] = i.a['href']
        searchResults.append(result)

    return searchResults  #returns a dictionary with all search results in it

# list = find_novel('my')
#
# for i in list:
#     print(i["name"])
#
# if(list == 404):
#     print('Novel Not found!')
# else:
#     for novels in list:
#         novelurl = novels['urlextension']
#         print(get_novel_text_by_url(novelurl, 1))
#         break


