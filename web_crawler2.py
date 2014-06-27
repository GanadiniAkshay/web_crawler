#web crawler 2.0

import urllib


def get_page(url):
    connection = urllib.urlopen(url)
    page = connection.read()
    return page


def get_next_link(string):
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

def get_all_links(page):
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


