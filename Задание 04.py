def prost(a):
    k=0
    lst=[]
    for i in range(1,a+1):
        if a%i==0:
            k=k+1
    if k==2:
        print('Число простое')
    else:
        print('Число не является простым')
