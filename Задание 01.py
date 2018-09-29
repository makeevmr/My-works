def rotate(a):
    if a>1:
        lst=[]
        result=[]
        for i in range(1,a+1):
            lst.append(i)
        k=lst[len(lst)-1]
        result.append(k)
        lst.pop()
        result.extend(lst)
        print(result)
    if a==0:
        lst=[]
        print(lst)
