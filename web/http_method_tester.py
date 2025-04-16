import requests
import sys

def test_http_methods(url):
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH', 'TRACE']
    print(f"\nTesting HTTP methods for: {url}\n")
    
    for method in methods:
        try:
            response = requests.request(method, url, timeout=5)
            print(f"{method}: {response.status_code} - {response.reason}")
            
            if method == 'OPTIONS':
                allowed_methods = response.headers.get('Allow', 'Not specified')
                print(f"Allowed Methods: {allowed_methods}")
                
        except requests.exceptions.RequestException as e:
            print(f"{method}: Error - {str(e)}")
        except Exception as e:
            print(f"{method}: Unexpected error - {str(e)}")

if len(sys.argv) != 2:
    print("Usage: python http_method_tester.py <url>")
    print("Example: python http_method_tester.py http://example.com")
    sys.exit(1)

url = sys.argv[1]
test_http_methods(url) 