from urllib.parse import urljoin
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from website import Page


class Spider():

    def __init__(self, url):
        self.url = url
        self.urls = [url]
        self.home_url = 'http://{}/'.format(url)
        self.visited = []

    def contain_hash_tag(url):
        if "#" in url:
            return True
        else:
            return False


    def _is_outgoing(url, tag):
        if url in tag:
            return False
        return True


    def prepare_link(home_url, href):
        return urljoin(home_url, href)

    def get_tags(this_url, website):
        r = requests.get(this_url)
        html = r.text

        soup = BeautifulSoup(html)
        if(soup.title and soup.description):
            website.pages.append(
                Page(url=this_url, title=soup.title.string, desc=soup.description.string))
            print("has title and desc")
        elif soup.title:
            website.pages.append(Page(url=this_url, title=soup.title.string))
            print("has title ")
        else:
            website.pages.append(Page(url=this_url))
            print("only url")

    def crawler(the_site):
        url = the_site
        urls = [url]
        visited = [url]

        while len(urls) > 0:
            try:
                htmltext = urlopen(urls[0]).read()
            except:
                print(urls[0])
            soup = BeautifulSoup(htmltext)
            urls.pop(0)
            for tag in soup.findAll('a', href=True):
                the_tag = Spider.prepare_link(url, tag['href'])
                if not Spider._is_outgoing(url, the_tag) and the_tag not in visited:
                    if not Spider.contain_hash_tag(the_tag):
                        visited.append(the_tag)
                        urls.append(the_tag)
            return visited

    def save_tags_db(all_urls, website):
        try:
            for url in all_urls:
                #print(url)
                Spider.get_tags(url, website)
        except requests.exceptions.MissingSchema:
            print("html")



