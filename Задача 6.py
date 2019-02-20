for a in range(1, 1000):
    for b in range(1, 1000):
        if ((a*a+b*b)/(a*b+1))%1 == 0:
            print(a, b, int((a*a+b*b)/(a*b+1)))
