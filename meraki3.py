# import json
# a='{"name":"David","class":"I","age": 6}'
# x=json.dumps(a)
# print(type(x))

import json
a={"name":"David","class":"I","age": 6}
f=open("meraki3.json","w")
json.dump(a,f,indent=4)
f.close()
