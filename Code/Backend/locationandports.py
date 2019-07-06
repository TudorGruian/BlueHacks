import socket
import json
import requests
import os


r = input("IP sau Domain? ")
adr = input("Introduce pricina ")


if r == "IP":
    pass
else:
    adr=socket.gethostbyname(adr)

print("Adresa este " + adr)

r = requests.get("http://ip-api.com/json/" + adr)
r = r.json()
country = str(r["country"])
city = str(r["city"])
isp = str(r["isp"])
region = str(r["region"])

print("Rezultat:")
print(country)
print(city)
print(isp)
print(region)

print("NMAP")
scanare_nmap = os.system("nmap " + adr + "> tmp")
scanare_nmap = open('tmp', 'r').read()
print(scanare_nmap)
os.remove('tmp')