def devider(a):
    k=0
    lst=[]
    for i in range(1,a+1):
        if a%i==0:
            lst.append(i)
            k=k+1
    print(lst)
