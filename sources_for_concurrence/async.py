import json
import time
import aiohttp
import asyncio
from os import path

file_value = 'values.json'
file_output = 'output.json'

if path.isfile(file_value) is False:
    raise Exception("File values.json not found")
if path.isfile(file_output) is False:
    raise Exception("File output.json not found")

try:
    with open(file_value, "r") as read_file:
        data = json.load(read_file)
        print("Successfully read file values.json")
except OSError:
    print("Not read file values.json")

#start time
start_time = time.time()

async def lead_time():
    async with aiohttp.ClientSession() as session:
        for x in range(len(data["start"])):
            url = "http://localhost:8080/primes?start={}&end={}".format(data["start"][x],data["end"][x])
            async with session.get(url) as resp:
                obj = await resp.read()
asyncio.run(lead_time())

#end time
exec_time = time.time() - start_time

print("--- exec synch %s seconds ---" % exec_time)

print_to_json = '{ "async" : %s }' % exec_time

try:
    with open(file_output, "w") as read_file:
        json.dump(print_to_json, read_file)
        print("Successfully write to the output.json")
except OSError:
    print("Not write to the output.json")
