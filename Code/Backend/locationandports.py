import socket
import json
import requests
import os
import websockets
import asyncio
#this is a test

async def hello(websocket,path):
    query = await websocket.recv()
    # print(f"< {name}")
    #
    # greeting = f"Hello {name}!"
    #
    # await websocket.send(greeting)
    # print(f"> {greeting}")
    process = query[-2:]
    adr = query[:-2]
    adr=socket.gethostbyname(adr)
    print("Adresa este " + adr)
    #lc at end = location
    if process == "lc":
        print("Se afla locatia")
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
        raspuns = ("Tara: " + country + ", Oras: " + city + ", ISP: " + isp + ",Regiune: " +region)
        await websocket.send(raspuns)

    #np at end = nmap
    if process == "np"
        print("NMAP")
        scanare_nmap = os.system("nmap " + adr + "> tmp")
        scanare_nmap = open('tmp', 'r').read()
        print(scanare_nmap)
        os.remove('tmp')
        await websocket.send(scanare_nmap)


start_server = websockets.serve(hello, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
