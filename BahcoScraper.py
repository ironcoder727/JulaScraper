import requests
from bs4 import BeautifulSoup

# URL of the product page
URL = 'https://www.jula.se/catalog/bil-och-garage/garage/lyftdon/domkrafter/hoglyftande-domkraft-002532/'

# Custom headers to mimic a browser request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

def get_price():
    # Send an HTTP request to the URL
    response = requests.get(URL, headers=HEADERS)

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the price element based on the provided structure
    price_element = soup.find('p', {'class': 'inline-block whitespace-nowrap text-right inline-block min-w-[1em] font-alt font-bold leading-none text-[4.5rem] text-greyDarker'})
    
    if price_element:
        # Extract text and clean up the formatting
        price = price_element.get_text(strip=True).replace("\u202f", "")  # Removes non-breaking spaces
        return price
    else:
        return "Price element not found"

# Monitor and print the price
if __name__ == "__main__":
    current_price = get_price()
    print(f"The current price of the product is: {current_price}")
