def word(str,wl,indices):
    el = wl-len(str)
    if el <0:
        return []
    elif el==0:
        return [].append(str)

    list1=[]
    for i in range(len(str)):
        for j in range(1,el+1):
            for m in range(i,len(str)):
                result=str[:m] + str[m]* (el-j)+ str[m:]
                result2=[x for x in result]
                result2.insert(i,str[i]*j)
                res="".join(result2)
                if res not in list1:
                    list1.append(res)
    list1.sort()
    if indices==[]:
        return list1

    final_result=[]
    for i in indices:
        final_result.append(list1[i])
    return final_result

string="1234"
length=6
item=[]
answer=word(string,length,item)
for i in answer:
    print(i)