# import requests
#
# response = requests.get('https://www.instagram.com/mr_bhaukali_mzp63')
# print("response code",response.status_code)
#
# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not Found.')
#-----------------------------------------------------------------------------------------------------------------------
#
# import requests
# from requests.exceptions import HTTPError
#
#
# for url in ['https://www.wscubetech.com/']:
#     try:
#         response = requests.get(url)
#
#         # If the response was successful, no Exception will be raised
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')
#
#         with open('file.html', 'wb') as file:
#             file.write(response.content)
#         print(response.cookies,response.text) #cookies,html content
#
#         ##get response headers and write 'request.header.txt'
#         print(response.headers)
#         with open('request.header.txt', 'w') as file:
#             file.write(str(response.headers))

#-----------------------------------------------------------------------------------------------------------------------

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
    file.write(str(headers))
