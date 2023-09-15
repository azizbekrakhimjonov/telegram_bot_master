# import requests
# response = requests.get(
#             'https://website.com/id',
#     headers={'Authorization': 'access_token myToken'})


# import urllib2
# response = urllib2.urlopen(
# urllib2.Request('https://website.com/id', headers={'Authorization': 'access_token myToken'})


# import requests
#
# myToken = '<token>'
# myUrl = '<website>'
# head = {'Authorization': 'token {}'.format(myToken)}
# response = requests.get(myUrl, headers=head)

# import requests
# response = requests.get('https://api.buildkite.com/v2/organizations/orgName/pipelines/pipelineName/builds/1230', headers={ 'Authorization': 'Bearer <your_token>' })
# print (response.json())

import requests
# respons = requests.get('https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/?ref=lbp')
# print(respons.text)

url = requests.get('https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/?ref=lbp')
text = url.text
print(text.split())