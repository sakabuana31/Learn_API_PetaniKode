import json
from urllib import request

# tentukan url endpoint
url = "https://api.github.com/users/sakabuana31"

# lakukan http request ke server
response = request.urlopen(url)

# parsing data json
data = json.loads(response.read())

# cetak hasil parsing data
# print(data)
print("")
print("-= Read Github API for My Profile =-")
print("")
print(f"Name: {data['name']}")
print(f"Company: {data['company']}")
print(f"Location: {data['location']}")
print(f"Git Repo: {data['public_repos']}")
print("")