from math import sqrt
ball1 = ()
ball2 = ()


def balls_collide(ball1, ball2):
    if ball1[3] < 0 or ball2[3] < 0:
        raise ValueError('Отрицательный радиус')
    x2, y2, z2, r2 = ball2[0], ball2[1], ball2[2], ball2[3]
    x1, y1, z1, r1 = ball1[0], ball1[1], ball1[2], ball1[3]
    if sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2) <= r1+r2:
        return True
    else:
        return False
