import urllib.parse
import requests

main_api = "http://ip-api.com/json/"
url = main_api
print("=============================================")
print("URL: " +url)
json_data = requests.get(url).json()
print("=============================================")
print("Public IP: " + (json_data["query"]))
print("Country: " + str(json_data["country"]))
print("Country Code: " + str(json_data["countryCode"]))
print("Region: " + str(json_data["regionName"]))
print("ISP: " + str(json_data["isp"]))
print("ASN & Provider: " + str(json_data["as"]))
print("=============================================")

