from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from connection import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from urllib.parse import urljoin
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import requests


class Website(Base):
    __tablename__ = "website"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    domain = Column(String)
    pages_count = Column(Integer)
    HTML_version = Column(Float)


class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True)
    website_url = Column(Integer, ForeignKey("website.url"))
    url = Column(String)
    title = Column(String)
    desc = Column(String)
    videos = Column(Integer)
    rating = Column(Integer)
    html5 = Column(Boolean)
    outgoin_links = Column(Integer)
    inner_links = Column(Integer)
    website = relationship(Website, backref="pages")

    def __str__(self):
        return "{} \n {}".format(self.title, self.url)

    def __repr__(self):
        return self.__str__()


class Spider():

    video_providers = ["https://www.youtube.com/",
                       "https://vimeo.com/",
                       "http://vbox7.com/",
                       "https://www.netflix.com/",
                       "http://www.dailymotion.com/",
                       "http://www.hulu.com/",
                       "http://vube.com/",
                       "http://www.twitch.tv/",
                       "http://www.liveleak.com/",
                       "https://vine.co/",
                       "http://www.ustream.tv/",
                       "http://www.viewster.com/",
                       "http://www.tv.com/",
                       "http://www.metacafe.com/"]
    # commands = {
    #     "search": Spider.search,
    #     "find": Spider.search_word,
    #     "exit": Spider.QUIT}

    html5_declaration = "<!DOCTYPE html>"
    temp_url = ""

    QUIT = False

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

    def _is_outgoing(tag):
        if Spider.temp_url in tag:
            return False
        return True

    def prepare_link(href):
        return urljoin(Spider.temp_url, href)

    def crawler(the_site):
        url = the_site
        Spider.temp_url = the_site
        urls = [url]
        visited = [url]

        while len(urls) > 0:
            r = requests.get(urls[0])
            htmltext = r.text
            soup = BeautifulSoup(htmltext)
            urls.pop(0)
            for tag in soup.findAll('a', href=True):
                the_tag = Spider.prepare_link(tag['href'])
                if not Spider._is_outgoing(the_tag) and the_tag not in visited:
                    if not Spider.contain_hash_tag(the_tag):
                        visited.append(the_tag)
                        urls.append(the_tag)
        return visited

    def save_tags_db(url, session):
        Spider.get_tags(url, session)

    def get_domain(url):
        parsed_uri = urlparse(url)
        base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        return base_url



    def quit(session):
        print("Bye bye")

    def execute_command(session):
        ui = input("Enter command >>>  ")
        Spider.commands[ui](session)

    def main():
        engine = create_engine("sqlite:///searchEngine.db")
        Base.metadata.create_all(engine)
        session = Session(bind=engine)
        try:
            while not Spider.QUIT:
                Spider.execute_command(session)
                #website = session.query(Website)
        except KeyError:
            print("Wrong menu , pls try again \n")
            Spider.execute_command(session)

    def get_tags(this_url, session):
        r = requests.request('GET', this_url)
        html = r.text

        soup = BeautifulSoup(html)
        try:
            title = soup.title.string
        except AttributeError:
            title = Spider.get_domain(this_url)

        description = soup.description
        Spider.temp_url = Spider.get_domain(this_url)

        html5 = Spider.is_html5(html)
        tags = soup.findAll('a', href=True)
        all_links = list(map(Spider.get_link_from_href, tags))
        prepared_links = list(map(Spider.prepare_link, all_links))
        outgoin_links = len(Spider.get_outgoin_links(prepared_links))
        video_links = len(Spider.get_video_links(prepared_links))
        blogs = len(Spider.get_blog_links(prepared_links))
        inner_links = len(prepared_links) - outgoin_links - video_links - blogs
        rating = Spider.define_rating(
            inner_links, outgoin_links, video_links, blogs, html5)

        session.add(Page(url=this_url, title=title, desc=description, rating=rating, videos=video_links,
                         html5=html5, outgoin_links=outgoin_links, inner_links=inner_links))
        session.commit()

    def get_video_links(prepared_links):
        return (set(list(filter(Spider.contain_video, prepared_links))))

    def get_blog_links(prepared_links):
        return (set(list(filter(Spider.is_blog, prepared_links))))

    def get_outgoin_links(prepared_links):
        return (set(list(filter(Spider._is_outgoing, prepared_links))))

    def define_rating(inner_links, outgoin_links, video_links, blogs, html5):
        rating = 0
        rating += inner_links * 0.1
        rating += outgoin_links * 0.075
        rating += video_links * 0.1
        rating += blogs * 0.1
        if html5:
            rating += 1
        print(rating)
        return rating

    def get_link_from_href(href):
        return href["href"]

    def is_html5(html_soup):
        return html_soup[0:15].lower() == Spider.html5_declaration.lower()

    def contain_video(href):
        if Spider._is_outgoing(href):
            domain = Spider.get_domain(href)
            if domain in Spider.video_providers:
                return True
            else:
                return False
        else:
            return False

    def is_blog(url):
        blog_type = "blog."
        return blog_type in url

    def get_video_page_urls(url):

        response = requests.get(url)
        soup = BeautifulSoup(response.text)

        for tag in soup.find_all(re.compile("^s")):
            print(tag)


    def sorter(list_of_sites):
        all_links = Spider.extend_list_of_sites(list_of_sites)
        return sorted(all_links, key=lambda page: page.rating, reverse=True)

    def extend_list_of_sites(list_of_sites):
        extendet_list_of_sites = []
        for site in list_of_sites:
            extendet_list_of_sites.extend(site)
        return extendet_list_of_sites


    def search_word(search_word):
        #search_word = input("What do you want to search? ")
        #search_word = search_word.split()
        engine = create_engine("sqlite:///searchEngine.db")
        session = Session(bind=engine)
        pages_searched = session.query(Page).filter(Page.title.like('%' + search_word + '%')).all()
        return set(pages_searched)

    def search(site):
        engine = create_engine("sqlite:///searchEngine.db")
        Base.metadata.create_all(engine)
        session = Session(bind=engine)
        #url = "http://hackbulgaria.com/"
        #url = input("Which site do you want to search? ")
        domain = Spider.get_domain(site)
        session.add(Website(url=domain))
        for link in Spider.crawler(site):
            Spider.save_tags_db(link, session)
            session.commit()

    def fulfil_db(list_of_new_sites):
        map(Spider.search(), list_of_sites)

if __name__ == '__main__':

    tu = "http://tu-sofia.bg/"
    sites = [tu, "http://aplus.com/"]
    visited = list(map(Spider.search, sites))
    # engine = create_engine("sqlite:///searchEngine.db")
    # Base.metadata.create_all(engine)
    # session = Session(bind=engine)
    # experiment = session.query(Page).filter(Page.title.like('%' + "hackbulgaria" + '%')).all()
    # print((list(experiment)))
    # sorteeed = (Spider.sorter(experiment))
    # print("\n\n\n\n")
    # print((sorteeed))

