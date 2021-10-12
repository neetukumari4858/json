import json
f1=open("meraki.7.txt","r")
f2=f1.readlines()
f=open("meraki7.json",mode="w")
json.dump(f2,f,indent=4)
f1.close()
f1.close()



