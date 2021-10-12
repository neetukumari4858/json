import json
d={"shopping_list":
        { 
            "chaco":15,
            "Biscuits":50,
            "Diary_milk":30,
            "ice_cream":20,
        } 
}
l=json.dumps(d)
print(type(l))
g=json.loads(l)
print("shoping list:-")
for i in g:
    for j in g[i]:
        print(j,g[i][j]) 
        
r=input("enter item which you want to pur:-")
m=int(input("how many items:-"))
for i in g:
    for j in g[i]:
        # print(g[i][j])
        if r=="chaco":
            v=g[i][j]-m
            g[i][j]=v
            break
        elif r=="Biscuits":
            v=g[i][j]-m
            g[i][j]=v
            break
        elif r=="Diary_milk":
            v=g[i][j]-m
            g[i][j]=v
            break
        elif r=="ice_cream":
            v=g[i][j]-m
            g[i][j]=v
            break
    print(g)
# print(g)



    # main dekhna chahta hu shopping list ko json file dekhna.

    # phir main user se poochu ga ki kon sa item khareedna chahte ho.

    # uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.

    # phir aapka wo number of items json file se remove karna hai.

    # Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.
