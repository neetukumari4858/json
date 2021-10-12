# import json
# a={"name": "David","class":"I","age": 6}
# x=json.dumps(a)
# print(type(x))

import json
ab={"name": "David","class":"I","age": 6}
f=open("meraki2.json","w")
json.dump(ab,f,indent=4)
f.close()


