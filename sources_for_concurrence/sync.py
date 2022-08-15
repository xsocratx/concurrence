import json
import time
import requests

with open("values.json", "r") as read_file:
    data = json.load(read_file)

start_time = time.time()

for x in range(len(data["start"])):
    print(data["start"][x])
    print(data["end"][x])
    print("---------")
    requests.get("http://localhost:8080/primes?start={}&end={}".format(data["start"][x],data["end"][x]))

exec_time = time.time() - start_time

print("--- sync - %s seconds ---" % exec_time)

print_to_json = '{ "sync" : %s }' % exec_time

with open("output.json","w") as read_file:
    json.dump(print_to_json, read_file)
