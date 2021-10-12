# 6. Write a Python program to create a new JSON file from an existing JSON file.
import json 
f1=open("hello.json","r")
f2=f1.readlines()
f=open("w3 6.json","w")
json.dump(f2,f,indent=4)
f1.close()
f.close()