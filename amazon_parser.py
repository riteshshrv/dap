import urllib.request
import json
from bs4 import BeautifulSoup, SoupStrainer


def crawler():
    '''Function that crawls entire website starting from the categories page.
       Function creates a list of links from all the pages it had crawled.'''
    
    to_crawl = []
    crawled = []
    # amazon category page
    l = 'http://www.amazon.in/gp/site-directory/ref=nav_shopall_btn'
    to_crawl.append(s)
    h = urllib.request.urlopen(l)
    crawled.append(s)

    soup = BeautifulSoup(h)
    for links in soup.fnd_all('a', href=True):
        if links.get('class', 'nav_a'):
            li = 'http://www.amazon.com' + links
            if li not in crawled:
                to_crawl.append(li)
    return to_crawl


def find_product_info(url=None):
    '''Function to find product information viz. name, price, description, image_path.
            Functi'''
    
    if url is None:
        mi_url = 'http://www.amazon.in/gp/product/B00VEB0F22?redirect=true&ref_=s9_acss_bw_sc_MiStore_ah_s1'
    soup = BeautifulSoup(urllib.request.urlopen(url))

    name = soup.find(id="productTtile").contents
    price = soup.find(id="priceblock_ourprice").get_text()
    description = soup.find(id="feature-bullets")
    img_path = soup.find(id="landingImage")
