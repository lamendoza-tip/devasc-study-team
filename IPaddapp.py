#PAJADURA, MENDOZA, TADIWAN

import urllib.parse
import requests

while True:
    print("Press Y if you want to check your own IP")
    print("Press N to quit")
    initial = input("Enter here: ")


    # =========================== Option 1 =========================== 
    if initial == "Y" or initial == "y":
        main_api = "http://ip-api.com/json/"
        url = main_api
        print("=============================================")
        print("URL: " +url)

        # Get JSON Data
        json_data = requests.get(url).json()
        print("=============================================")
        print("Public IP: " + (json_data["query"]))
        print("Country: " + str(json_data["country"]))
        print("Country Code: " + str(json_data["countryCode"]))
        print("Region: " + str(json_data["regionName"]))
        print("ISP: " + str(json_data["isp"]))
        print("ASN & Provider: " + str(json_data["as"]))
        print("=============================================")


    # =========================== Option 2 =========================== 
    if initial == "N" or initial == "n":
        break
