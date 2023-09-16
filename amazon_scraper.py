import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

def fetch_amazon_product_details(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        
        product_title = soup.find(id='productTitle').get_text().strip()
        product_price = soup.find(id='priceblock_ourprice').get_text().strip()

        return {
            'Title': product_title,
            'Price': product_price
        }
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

if __name__ == '__main__':
    product_url = input("Enter the Amazon product URL: ")
    details = fetch_amazon_product_details(product_url)
    print(details)
