def calc(a,b,c):
    k=0
    if b=='+':
        print(a+c)
        k=k+1
    else:    
        if b=='*':
            print(a*c)
            k=k+1
        else:    
            if b=='-':
                print(a-c)
                k=k+1
            else:
                if b=='/':
                    print(a/c)
                    k=k+1
                else:
                    try:
                        p=1/k
                    except:
                        print('Выбранная операция не соответствует условию')
