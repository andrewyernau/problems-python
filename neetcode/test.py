dict= {"Hola":[1,2,4],"Parte":2}
print(len(list(dict.keys()))-1)
print("###TEST 2 ###")
ls= list()
ls2= ["a","b","c"]
ls3= [1,2,3]
ls = [ls2,ls3]
print(ls)

indexof= ls.index(["a","b","c"])
##print (indexof)

##print(str(ls2))
##print(''.join(ls2))
print(dict.keys())
print(dict.values())
if 1 in dict.values():
    print("hola")
nums=[1,2,2,3,3,3]
freq = [[] for i in range(len(nums) + 1)]
print(freq)