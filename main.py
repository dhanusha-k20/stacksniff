import requests

url = input("Enter target URL: ").strip()

try:
    response = requests.get(url, timeout=5)

    print("URL:", response.url)
    print("Status:", response.status_code)
    print("Body length:", len(response.text))
    print("Headers:")
    for name, value in response.headers.items():
        print(f"  {name}: {value}")

except requests.exceptions.RequestException as e:
    print(f"Could not reach {url}: {e}")
