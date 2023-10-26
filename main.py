import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import re

url = 'https://www.wscubetech.com/'

try:
    response = requests.get(url)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')

    with open('file.html', 'wb') as file:
        file.write(response.content)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]

    with open('urls.txt', 'w') as urls_file:
        for link in links:
            urls_file.write(link + '\n')

    print(response.cookies)

headers = response.headers
print(headers)
with open('request.header.txt', 'w') as file:
    file.write(str(headers)
