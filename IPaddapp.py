import urllib.parse
import requests

main_api = "http://ip-api.com/json/"
url = main_api
print("=============================================")
print("URL: " +url)
json_data = requests.get(url).json()
print("=============================================")
print(json_data)
print("=============================================")