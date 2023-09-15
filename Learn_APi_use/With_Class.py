# import json

# from requests.auth import AuthBase
# import requests
#
#
# class TokenAuth(AuthBase):
#     def __init__(self, token, auth_scheme='Bearer'):
#         self.token = token
#         self.auth_scheme = auth_scheme
#
#     def __call__(self, request):
#         request.headers['Authorization'] = f'{self.auth_scheme} {self.token}'
#         return request
#
# response = requests.get(
#     url='https://github.com/fawazahmed0/quran-api',
#     auth=TokenAuth(token='abcde', auth_scheme='access_token'),
# )
# response.encoding = 'utf-8'
# response.json()
# response.headers()
# print(response.json())
#
#
#
#
# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not Found.')


import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# requests.post('https://httpbin.org/post', data={'key':'value'})
# requests.put('https://httpbin.org/put', data={'key':'value'})
# requests.delete('https://httpbin.org/delete')
# requests.head('https://httpbin.org/get')
# requests.patch('https://httpbin.org/patch', data={'key':'value'})
# requests.options('https://httpbin.org/get')

# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Text matches: {repository["text_matches"]}')

# requests.delete('https://httpbin.org/delete')
json_response = response.json()
print(json_response['args'])

