import json
d='{"a":1,"a":2,"a":3, "a":4,"b":1, "b":2}'
x=json.loads(d)
f=open("meraki6.json","w")
json.dump(x,f)
f.close()



