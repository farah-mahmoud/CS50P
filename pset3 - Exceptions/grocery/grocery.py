#https://cs50.harvard.edu/python/2022/psets/3/grocery/


mylist = []
mydict = {}
while True:
    try:
        grocery_list = input().upper()
        mylist.append(grocery_list)
    except EOFError:
        break
mylist.sort()
#print(mylist)
for item in mylist:
    counter = mylist.count(item)
    mydict.update({item: counter})
#print(mydict)
for k, v in mydict.items():
    print(v, k)

