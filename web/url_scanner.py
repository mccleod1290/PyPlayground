import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def scan_url(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print(f"\nScanning: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Server: {response.headers.get('Server', 'Not Found')}")
        
        forms = soup.find_all('form')
        print(f"\nFound {len(forms)} forms")
        for form in forms:
            print(f"Form action: {form.get('action', 'No action')}")
            print(f"Method: {form.get('method', 'GET')}")
            
        links = soup.find_all('a')
        print(f"\nFound {len(links)} links")
        
    except Exception as e:
        print(f"Error scanning {url}: {str(e)}")

url = input("Enter URL to scan (include http/https): ")
scan_url(url) 