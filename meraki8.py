x=[["neelam","programer","24","2400"],
["komal","trainer","24","20000"],
["anuradha","HR","25","40000"],
["Abhishek","manager","29","63000"]]
# emp1 emp2 emp3 and emp4.keys
import json
d1={}

# key=input("enter outer key user:-")
i=0
while i<len(x):
    key=input("enter outer key user:-")
    d={}
    j=0
    while j<len(x[i]):
        a=x[i][0]
        b=x[i][1]
        c=x[i][2]
        e=x[i][3]
        j=j+1
        d["name"]=a
        d["deshtination"]=b
        d["age"]=c
        d["salary"]=e
    i=i+1
    d1[key]=d
print(d1)
f=open("meraki8.json","w")
json.dump(d1,f,indent=4)
f.close()



# x=[["neelam","programer","24","2400"],
# ["komal","trainer","24","20000"],
# ["anuradha","HR","25","40000"],
# ["Abhishek","manager","29","63000"]]
# # emp1 emp2 emp3 and emp4.keys
# import json
# d={}
# d1={}
# # # n=int(input("enter no:-"))
# # for i in range(1,5):
# # key=input("enter outer key user:-")
# i=0
# while i<len(x):
    
#         a=x[i][0]
#         b=x[i][1]
#         c=x[i][2]
#         e=x[i][3]
#         key=input("enter outer key user:-")
#         d["name"]=a
#         d["deshtination"]=b
#         d["age"]=c
#         d["salary"]=e
#         d1[key]=d
#         i=i+1
# print(d1)