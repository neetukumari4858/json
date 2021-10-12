# import json
# x='{"Name":"Ram","Class":"IV","Age":9 }'
# y=json.loads(x)
# print(type(y))

import json
xy={"Name":"Ram","Class":"IV","Age":9 }
f=open("meraki1.json","w")
json.dump(xy,f,indent=4)
f.close()



