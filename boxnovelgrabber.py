from bs4 import BeautifulSoup as bs
import requests
import html5lib

url = "https://boxnovel.com/novel/nano-machine-retranslated-version/"
def getnoveltext(novelurl, chapternumber):
    url = novelurl + "/chapter-" + chapternumber
    data = requests.get(url)

    soup = bs(data.content, 'html5lib')
    rawtext = soup.find('div', attrs={'class':'reading-content'})
    print(rawtext.get_text())

def searchnovels(novelname):
    searchresults = []
    url = "https://boxnovel.com/?s=" + novelname.replace(" ","+") + "&post_type=wp-manga"
    data = requests.get(url)

    soup = bs(data.content, 'html5lib')

    for items in soup.findAll('div', attrs={'class':'post-title'}):
        search = {}
        search['name'] = items.h4.text
        search['url']=items.h4.a['href']
        searchresults.append(search)

    return searchresults

# for i in range(100):
#     print(searchnovels('my')[i]['url'])
#     if(searchnovels('my')[i]['url']) == None:
#         break

