import requests
from bs4 import BeautifulSoup


def response(url):
    return requests.get(url)


def soup(res):
    return BeautifulSoup(res.text, 'html.parser')


def links(param):
    return param.select('.storylink')


def subtext(param):
    return param.select('.subtext')


res1 = response('https://news.ycombinator.com/news')
res2 = response('https://news.ycombinator.com/news?p=2')
res3 = response('https://news.ycombinator.com/news?p=3')
soup1 = soup(res1)
soup2 = soup(res2)
soup3 = soup(res3)


mega_links = links(soup1) + links(soup2) + links(soup3)
mega_subtext = subtext(soup1) + subtext(soup2) + subtext(soup3)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def custom_hackernews(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


print(custom_hackernews(mega_links, mega_subtext))
