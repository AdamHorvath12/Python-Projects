import csv
from bs4 import BeautifulSoup
from selenium import webdriver


def get_url(search_item):
    #Generate a url from search term
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
    search_item = search_item.replace(' ', '+')
    url = template.format(search_item)
    ## add page query placeholder
    url +='&page{}'
    return url

def extract_details(item):
    #extract and return details
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')
    try:
        price_parent = item.find('span','a-price')
        price = price_parent.find('span','a-offscreen').text
    except AttributeError:
        return
    
    try:
        rating = item.i.text
    except AttributeError:
        rating = '-'
    
    try:
        review_count = item.find('span',{'class':'a-size-base','dir':'auto'}).text
    except AttributeError:
        review_count = '-'
    return (description,price,rating,review_count, url)

def main(serach_term):
    driver = webdriver.Chrome(r"C:\Users\Lenovo\OneDrive\Asztali gép\chromedriver_win32\chromedriver.exe")
    
    records = []
    url = get_url('apple ipad pro')
    for page in range(1,21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_details(item)
            if record:
                records.append(record)
    driver.close()

    with open('amazon_result.csv','w',newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Deescription','Price','Rating','ReviewCount','URL'])
        writer.writerows(records)

main('apple ipad pro')