n=int(input())
answer=[]
for i in range(n):
    lan=list(input())
    lan2=[]
    for i in range(len(lan)-1,-1,-1):
        lan2.append(lan[i])
    for i in range(len(lan)):
        tmp=lan.copy()
        tmp2=''.join(i for i in lan2)
        del tmp[0:i]
        tmp=''.join(i for i in tmp)
        if tmp in tmp2:
            tmp2=list(tmp2)
            del tmp2[0:len(lan2)-i]
            lan=''.join(i for i in lan)
            tmp2=''.join(i for i in tmp2)
            lan+=tmp2
            break
    answer.append(lan)
for i in answer:
    print(i)