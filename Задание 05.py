def palindrom(s):
    k=0
    f=len(s)-1
    n=0
    if len(s)>1:
        for i in range(1,len(s)//2+1):
            if s[k]==s[f]:
                n=n+1
            if s[k]<s[f] or s[k]>s[f]:
                print('Строка не является палиндромом')
                break
            k=k+1
            f=f-1
    if n==len(s)//2:
        print('Строка является палиндромом')
    if len(s)<2:
        print('Строка не является палиндромом')
