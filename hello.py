# json file to python object:-(already json file)
import json
file =open("hello.json","r")
data=json.load(file)
print(data)
print(type(data))
