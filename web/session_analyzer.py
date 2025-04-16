import requests
import json

def analyze_session(url):
    try:
        response = requests.get(url)
        cookies = response.cookies
        headers = response.headers
        
        print("\nSession Analysis Results:")
        print("\nCookies:")
        for cookie in cookies:
            print(f"Name: {cookie.name}")
            print(f"Value: {cookie.value}")
            print(f"Domain: {cookie.domain}")
            print(f"Secure: {cookie.secure}")
            print(f"HttpOnly: {cookie.has_nonstandard_attr('HttpOnly')}")
            print("---")
            
        print("\nSecurity Headers:")
        security_headers = ['X-Frame-Options', 'X-XSS-Protection', 
                          'X-Content-Type-Options', 'Strict-Transport-Security']
        for header in security_headers:
            value = headers.get(header, 'Not Set')
            print(f"{header}: {value}")
            
    except Exception as e:
        print(f"Error analyzing session: {str(e)}")

url = input("Enter URL to analyze (include http/https): ")
analyze_session(url) 