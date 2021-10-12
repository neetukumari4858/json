# import json
# d={'4': 5, 
#    '6': 7,
#    '1': 3,
#    '2': 4}
# d1={}
# for i,j in  sorted (d.items()):
#     d1[i]=j
# x=json.dumps(d1)
# print(x)
# print(type(x))

import json
d={'4': 5, 
   '6': 7,
   '1': 3,
   '2': 4}
d1={}
for i,j in  sorted (d.items()):
    d1[i]=j
f=open("meraki4.json","w")
json.dump(d1,f,indent=4)
f.close()






 