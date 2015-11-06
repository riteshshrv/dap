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
	# This Function currently only works for one url
    '''Function to find product information viz. name, price, description, image_path.
        
        Function takes an input url and dumps info of only the product available 
        in that page. If 'url' is None than function starts generating data from 
        crawler.'''
    
    if url is None:
        url = 'http://www.amazon.in/gp/product/B00VEB0F22?redirect=true&ref_=s9_acss_bw_sc_MiStore_ah_s1'
    soup = BeautifulSoup(urllib.request.urlopen(url))

    name = soup.find(id="productTitle").contents
    price = soup.find(id="priceblock_ourprice").get_text().split()[-1]

    description_markup = soup.find(id="feature-bullets")
    description=[]
    for i in description_markup.ul.find_all('span'):
    	description.append(''.join(i.contents))

    category=soup.find('span',{"class":"a-list-item"}).a.contents
    img_path = soup.find(id="landingImage")

    data=[]
    data.append({
    	"name": name,
    	"price": price,
    	"description": description,
    	"img": img_path,
    	"category": category
    	})
    with open("my_output.json","w") as outf:
    	json.dumps(data,outf)

if __name__ == '__main__':
	print("Work in progress")
	try:
		find_product_info()
		print("please check 'my_output.json' file in current path for output data.")
	except:
		print("something wrong happened.")
		raise NotImplementedError