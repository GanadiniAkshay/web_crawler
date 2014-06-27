#web crawler 3.0

#importing the url library to use urlopen functionality
import urllib

#function to get the contents of a page
def get_page(url):
    """Takes an input URL and returns the html contents """
    connection = urllib.urlopen(url)
    page = connection.read()
    return page

#function to extract the next link from site
def get_next_link(string):
    """Takes as input html and returns the first link in that html"""
    start_pos = string.find('<a href="')
    if start_pos == -1:
        start_pos = string.find("<a href='")
        if start_pos == -1:
            return None,0
        start_quote = start_pos + 8
        end_quote = string.find("'",start_quote+1)
        url = string[start_quote+1:end_quote]
        return url,end_quote+1
    start_quote = start_pos + 8
    end_quote = string.find('"',start_quote+1)
    url = string[start_quote+1:end_quote]
    return url,end_quote+1


#function to extract all links from a site
def get_all_links(page):
    """Takes as input contents of a webpage and returns a list of all links on the site"""
    urls=[]
    while True:
        url,endpos = get_next_link(page)
        if url:
            if not url == '#':
                urls.append(url)
            page = page[endpos:]
        else:
            break
    return urls

#function to crawl the web 
def crawl(seed,limited=True,depth=1):
    """Takes as input a seed url and crawls the web using this as a base site"""
    i=0
    toCrawl = [seed]
    crawled = []
    prev_site = seed
    if limited==False:
        while not len(toCrawl)==0:
            site = toCrawl.pop()
            if site in crawled:
                continue
            if site[0] == '/':
                site = prev_site+site
            elif site[0] == ".":
                continue
            elif site[0] == "h":
                site = site
            else:
                continue
            page = get_page(site)
            links = get_all_links(page)
            crawled.append(site)
            for link in links:
                toCrawl.append(link)
            prev_site=site
            print prev_site
        return crawled
    else:
        while i<depth:
            site = toCrawl.pop()
            if site in crawled:
                continue
            if site[0] == '/':
                site = prev_site+site
            elif site[0] == ".":
                continue
            elif site[0] == "h":
                site = site
            else:
                continue
            page = get_page(site)
            links = get_all_links(page)
            crawled.append(site)
            for link in links:
                toCrawl.append(link)
            i+=1
            prev_site=site
        return crawled
            



